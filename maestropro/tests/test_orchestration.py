"""
Tests for the Full Orchestration Workflow
(SheetSage2 + YuE2 + Human-in-the-Loop).
"""

import textwrap
from pathlib import Path

import pytest

from backend.orchestration.abc_bridge import (
    AbcBridgeError,
    parse_lead_sheet,
    strip_chords,
)
from backend.orchestration.abc_export import (
    decompose_duration,
    score_to_native_abc,
)
from backend.orchestration.chords import chord_pitches, figure_to_native, parse_native_chord
from backend.orchestration.models import (
    ArrangementConfig,
    EditRegisteredRequest,
    OrchestrationSession,
    OrchestrationStage,
)
from backend.orchestration.score_builder import (
    build_orchestration_score,
    export_musicxml,
)
from backend.orchestration.session import (
    ALLOWED_TRANSITIONS,
    SessionError,
    SessionStore,
    StageTransitionError,
    transition,
)
from backend.orchestration.sheetsage2 import SheetSage2Adapter
from backend.orchestration.yue2 import YuE2Adapter

# Valid native two-voice ABC fixture (meets abc_tools.parse invariants)
NATIVE_ABC_FIXTURE = textwrap.dedent("""\
    X:1
    T:
    M:4/4
    L:1/32
    Q:1/4=96
    V: Vocal clef=treble name="Vocal Melody" snm="Vocal"
    V: Ins clef=treble name="Ins Melody" snm="Inst."
    K:C
    V: Vocal
    "C"C8 D8 E8 G8|"Cmaj7"c8 B8 A8 G8|
    V: Ins
    Z|Z|
""")


@pytest.fixture()
def lead_sheet():
    return parse_lead_sheet(NATIVE_ABC_FIXTURE)


@pytest.fixture()
def arrangement_config():
    return ArrangementConfig(
        genre="String Orchestra",
        instruments=["Violin I", "Viola", "Cello"],
        tempo=96,
    )


@pytest.fixture()
def orchestration_score(lead_sheet, arrangement_config):
    return build_orchestration_score(lead_sheet, arrangement_config)


# ---------------------------------------------------------------------------
# Native ABC bridge
# ---------------------------------------------------------------------------

class TestAbcBridge:
    def test_fixture_parses(self, lead_sheet):
        assert lead_sheet.bpm == 96
        assert lead_sheet.meter == "4/4"
        assert lead_sheet.key == "C"
        assert len(lead_sheet.melody) == 8
        assert [n.pitch for n in lead_sheet.melody] == [
            60, 62, 64, 67, 72, 71, 69, 67,
        ]
        assert [c.symbol for c in lead_sheet.chords] == ["C", "Cmaj7"]

    def test_invalid_abc_raises(self):
        with pytest.raises(AbcBridgeError):
            parse_lead_sheet("not a real abc file")

    def test_strip_chords(self):
        stripped = strip_chords(NATIVE_ABC_FIXTURE)
        body = stripped.split("K:C", 1)[1]
        assert '"' not in body
        # Melody preserved
        again = parse_lead_sheet(stripped)
        assert [n.pitch for n in again.melody] == [
            60, 62, 64, 67, 72, 71, 69, 67,
        ]
        assert again.chords == []


# ---------------------------------------------------------------------------
# Chord mapping
# ---------------------------------------------------------------------------

class TestChords:
    @pytest.mark.parametrize("figure,expected", [
        ("C", "C"),
        ("Cmaj7", "Cmaj7"),
        ("Cm", "Cm"),
        ("Cmin7", "Cm7"),
        ("C7", "C7"),
        ("F#m7b5", "F#m7b5"),
        ("Bb7", "Bb7"),
        ("Ebmaj7", "Ebmaj7"),
        ("C/G", "C/G"),
        ("G7sus4", "G7sus4"),
        ("Adim", "Adim"),
        ("C+", "Caug"),
    ])
    def test_figure_to_native(self, figure, expected):
        assert figure_to_native(figure) == expected

    def test_unsupported_returns_none(self):
        assert figure_to_native("") is None

    def test_parse_native_chord(self):
        parsed = parse_native_chord("Cmaj7")
        assert parsed == (0, "maj7", None)
        slash = parse_native_chord("C/G")
        assert slash == (0, "", 7)

    def test_chord_pitches_include_root_and_third(self):
        pitches = chord_pitches("C")
        assert pitches is not None
        assert any(p % 12 == 0 for p in pitches)
        assert any(p % 12 == 4 for p in pitches)


# ---------------------------------------------------------------------------
# Score builder (step [3]: lead sheet → multi-part MusicXML)
# ---------------------------------------------------------------------------

class TestScoreBuilder:
    def test_part_count_and_names(self, orchestration_score):
        assert len(orchestration_score.parts) == 3
        names = [p.partName for p in orchestration_score.parts]
        assert names == ["Violin I", "Viola", "Cello"]

    def test_melody_carried_by_first_instrument(self, orchestration_score, lead_sheet):
        first = orchestration_score.parts[0]
        notes = [n for n in first.recurse().notes if hasattr(n, "pitch")]
        original = [n.pitch for n in lead_sheet.melody]
        # Melody material must all appear in the first part
        produced = [n.pitch.midi for n in notes]
        for pitch in original:
            assert pitch in produced

    def test_harmony_parts_receive_chord_tones(self, orchestration_score):
        for part in orchestration_score.parts[1:]:
            notes = [n for n in part.recurse().notes if hasattr(n, "pitch")]
            assert len(notes) > 0, f"{part.partName} received no notes"

    def test_export_musicxml_roundtrip(self, orchestration_score, tmp_path):
        out = tmp_path / "score.musicxml"
        export_musicxml(orchestration_score, out)
        assert out.is_file()
        assert out.stat().st_size > 500

        from music21 import converter
        reloaded = converter.parse(str(out))
        assert len(reloaded.parts) == 3

    def test_empty_melody_rejected(self, arrangement_config):
        from backend.orchestration.abc_bridge import LeadSheet
        empty = LeadSheet(bpm=120, meter="4/4", key="C", melody=[])
        with pytest.raises(Exception):
            build_orchestration_score(empty, arrangement_config)


# ---------------------------------------------------------------------------
# Round trip: score → native ABC (preview conditioning)
# ---------------------------------------------------------------------------

class TestAbcExport:
    def test_decompose_duration(self):
        for units in (1, 5, 7, 10, 31, 48, 50, 100, 128):
            pieces = decompose_duration(units)
            assert sum(pieces) == units
            assert all(p in {1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48} for p in pieces)

    def test_score_to_native_abc_validates(self, orchestration_score):
        abc_text = score_to_native_abc(orchestration_score, bpm=96)
        assert abc_text.startswith("X:1\nT:\nM:4/4\n")
        assert "L:1/32" in abc_text
        assert "Q:1/4=96" in abc_text

        # Must satisfy the strict native parser
        reparsed = parse_lead_sheet(abc_text)
        assert reparsed.bpm == 96
        assert reparsed.meter == "4/4"
        assert len(reparsed.melody) == 8
        assert [n.pitch for n in reparsed.melody] == [
            60, 62, 64, 67, 72, 71, 69, 67,
        ]
        assert [c.symbol for c in reparsed.chords] == ["C", "Cmaj7"]

    def test_musicxml_file_to_abc(self, orchestration_score, tmp_path):
        out = tmp_path / "score.musicxml"
        export_musicxml(orchestration_score, out)

        from music21 import converter
        reloaded = converter.parse(str(out))
        abc_text = score_to_native_abc(reloaded, bpm=96)
        reparsed = parse_lead_sheet(abc_text)
        # Melody pitches survive the MusicXML → ABC hop
        original = [60, 62, 64, 67, 72, 71, 69, 67]
        produced = [n.pitch for n in reparsed.melody]
        assert produced == original

    def test_chord_free_export_for_melody_mode(self, orchestration_score):
        abc_text = score_to_native_abc(orchestration_score, bpm=96)
        stripped = strip_chords(abc_text)
        reparsed = parse_lead_sheet(stripped)
        assert reparsed.chords == []
        assert len(reparsed.melody) == 8


# ---------------------------------------------------------------------------
# Session state machine (human-in-the-loop)
# ---------------------------------------------------------------------------

class TestSessionStateMachine:
    @pytest.fixture()
    def store(self, tmp_path):
        return SessionStore(tmp_path / "orchestration")

    @pytest.fixture()
    def session(self, store, arrangement_config):
        return store.create("song.mp3", arrangement_config)

    def test_create_starts_configured(self, session):
        assert session.stage == OrchestrationStage.CONFIGURED
        assert session.edit_revision == 0
        assert session.previews == []

    def test_happy_path_transitions(self, session):
        transition(session, OrchestrationStage.TRANSCRIBING)
        transition(session, OrchestrationStage.AWAITING_EDIT)
        transition(session, OrchestrationStage.PREVIEWING)
        transition(session, OrchestrationStage.PREVIEW_READY)
        # Human edits again → iterate
        session.edit_revision += 1
        transition(session, OrchestrationStage.AWAITING_EDIT)
        transition(session, OrchestrationStage.PREVIEWING)
        transition(session, OrchestrationStage.PREVIEW_READY)
        transition(session, OrchestrationStage.EXPORTED)
        assert session.stage == OrchestrationStage.EXPORTED

    def test_illegal_transition_raises(self, session):
        with pytest.raises(StageTransitionError):
            transition(session, OrchestrationStage.PREVIEWING)  # configured → previewing

    def test_error_recovery(self, session):
        transition(session, OrchestrationStage.TRANSCRIBING)
        transition(session, OrchestrationStage.ERROR)
        transition(session, OrchestrationStage.TRANSCRIBING)
        assert session.stage == OrchestrationStage.TRANSCRIBING

    def test_every_stage_has_transitions(self):
        for stage in OrchestrationStage:
            assert stage in ALLOWED_TRANSITIONS

    def test_persistence_reload(self, store, session, tmp_path):
        transition(session, OrchestrationStage.TRANSCRIBING)
        transition(session, OrchestrationStage.AWAITING_EDIT)
        store.save(session)

        reloaded = SessionStore(tmp_path / "orchestration")
        restored = reloaded.get(session.session_id)
        assert restored.stage == OrchestrationStage.AWAITING_EDIT
        assert restored.config.instruments == ["Violin I", "Viola", "Cello"]

    def test_unknown_session(self, store):
        with pytest.raises(SessionError):
            store.get("orc_missing")


# ---------------------------------------------------------------------------
# Adapters (availability + request building)
# ---------------------------------------------------------------------------

class TestAdapters:
    def test_sheetsage2_unconfigured(self, tmp_path):
        from backend.config import Settings
        cfg = Settings(
            SHEETSAGE2_SKILL_DIR=Path(__file__).resolve().parents[2] / "yue2-music",
            SHEETSAGE2_PYTHON="",
            ORCHESTRATION_DIR=tmp_path / "orc",
        )
        adapter = SheetSage2Adapter(cfg)
        health = adapter.health()
        assert health["available"] is False
        assert health["configured"] is False
        assert "SHEETSAGE2_PYTHON" in health["detail"]
        # Script itself ships with the repo
        assert adapter.script.is_file()

    def test_yue2_unconfigured(self, tmp_path):
        from backend.config import Settings
        cfg = Settings(
            YUE2_SKILL_DIR=Path(__file__).resolve().parents[2] / "yue2-music",
            YUE2_PYTHON="",
            ORCHESTRATION_DIR=tmp_path / "orc",
        )
        adapter = YuE2Adapter(cfg)
        health = adapter.health()
        assert health["available"] is False
        assert "YUE2_PYTHON" in health["detail"]
        assert adapter.script.is_file()

    def test_build_preview_request(self):
        adapter = YuE2Adapter()
        request = adapter.build_request(
            session_id="orc_test",
            genre="String Orchestra",
            instruments=["Violin I", "Viola", "Cello"],
            tempo=96,
            style_prompt=None,
            lyrics=None,
        )
        assert request["id"] == "orchestrate_orc_test"
        assert "String Orchestra" in request["style"]
        assert "96 BPM" in request["style"]
        assert "Violin I" in request["style"]
        assert request["lyrics"].startswith("[Verse]")
        assert isinstance(request["seed"], int)

        custom = adapter.build_request(
            session_id="x", genre="Jazz", instruments=["Trumpet"],
            tempo=120, style_prompt="cool jazz", lyrics="[Verse]\nHello world",
        )
        assert custom["style"] == "cool jazz"
        assert custom["lyrics"] == "[Verse]\nHello world"
