/*
 * MaestroPro - Main Dashboard UI
 * Maya Instruments Technology
 * Version: 1.0.0
 * 
 * Professional dark mode interface with Deep Blue (#1a3a52) and Gold (#d4af37) accents.
 * MuseScore 4 Plugin (Qt 6 / QtQuick)
 */

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.15

Rectangle {
    id: root
    width: 450
    height: 700
    color: "#0d1b2a"  // bgDark
    
    // Theme Constants
    readonly property color primary: "#1a3a52"      // Deep Blue
    readonly property color accent: "#d4af37"       // Gold
    readonly property color bgCard: "#1b2838"
    readonly property color textPrimary: "#ffffff"
    readonly property color textSecondary: "#a0aec0"
    readonly property color success: "#48bb78"
    readonly property color error: "#fc8181"
    readonly property int borderRadius: 8
    
    // WebSocket connection state
    property bool wsConnected: false
    property string wsStatus: "Disconnected"
    
    // Current task state
    property string currentTaskId: ""
    property int currentProgress: 0
    property string currentStage: ""
    property string statusMessage: "Ready"
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 16
        
        // ==================== HEADER ====================
        RowLayout {
            Layout.fillWidth: true
            spacing: 12
            
            // Logo Icon (placeholder)
            Rectangle {
                width: 40
                height: 40
                radius: 8
                color: root.accent
                
                Text {
                    anchors.centerIn: parent
                    text: "🎼"
                    font.pixelSize: 24
                }
            }
            
            ColumnLayout {
                Layout.fillWidth: true
                spacing: 2
                
                Label {
                    text: "MaestroPro"
                    font.pixelSize: 26
                    font.bold: true
                    font.family: "Playfair Display"
                    color: root.accent
                    elide: Text.ElideRight
                }
                
                Label {
                    text: "Maya Instruments Technology"
                    font.pixelSize: 11
                    color: root.textSecondary
                    font.italic: true
                }
            }
            
            // Connection Status Indicator
            Rectangle {
                width: 10
                height: 10
                radius: 5
                color: root.wsConnected ? root.success : root.error
                
                ToolTip.visible: hovered
                ToolTip.text: root.wsConnected ? "Backend Connected" : "Backend Disconnected"
                
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: checkConnection()
                }
            }
        }
        
        // Tagline
        Label {
            text: "\"From Audio to Artistry\""
            font.pixelSize: 13
            color: root.textSecondary
            font.italic: true
            horizontalAlignment: Text.AlignHCenter
            Layout.fillWidth: true
        }
        
        // ==================== TRANSCRIBE SECTION ====================
        Rectangle {
            Layout.fillWidth: true
            height: 160
            color: root.bgCard
            radius: root.borderRadius
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 16
                spacing: 12
                
                // Section Header
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    Text {
                        text: "📥 TRANSCRIBE"
                        font.pixelSize: 16
                        font.bold: true
                        color: root.primary
                    }
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: root.primary
                        opacity: 0.3
                    }
                }
                
                // YouTube URL Input
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    TextField {
                        id: urlInput
                        Layout.fillWidth: true
                        placeholderText: "YouTube URL or paste audio link..."
                        color: root.textPrimary
                        font.pixelSize: 13
                        
                        background: Rectangle {
                            color: root.primary
                            radius: 4
                            opacity: 0.5
                        }
                        
                        onTextChanged: {
                            if (text.length > 0) {
                                transcribeButton.enabled = true
                            } else {
                                transcribeButton.enabled = false
                            }
                        }
                    }
                    
                    Button {
                        id: browseButton
                        text: "Browse"
                        enabled: !root.wsConnected
                        palette.button: root.primary
                        palette.buttonText: root.textPrimary
                        
                        onClicked: {
                            statusMessage = "Opening file dialog..."
                            // In production: trigger file picker via MuseScore API
                        }
                    }
                }
                
                // Options Row
                RowLayout {
                    spacing: 16
                    
                    CheckBox {
                        id: separateStemsCheckbox
                        text: "Separate Stems"
                        checked: true
                        palette.buttonText: root.textSecondary
                        font.pixelSize: 12
                    }
                    
                    ComboBox {
                        id: quantizeGridCombo
                        model: ["1/8", "1/16", "1/32"]
                        currentIndex: 1
                        palette.button: root.primary
                        palette.buttonText: root.textPrimary
                        font.pixelSize: 12
                        
                        Label {
                            anchors.left: parent.left
                            anchors.top: parent.bottom
                            text: "Quantize:"
                            font.pixelSize: 11
                            color: root.textSecondary
                        }
                    }
                }
                
                // Transcribe Button
                Button {
                    id: transcribeButton
                    text: "▶ Transcribe"
                    Layout.fillWidth: true
                    enabled: false
                    palette.button: root.accent
                    palette.buttonText: "#000000"
                    font.bold: true
                    font.pixelSize: 14
                    
                    background: Rectangle {
                        color: transcribeButton.pressed ? "#b8962e" : root.accent
                        radius: root.borderRadius
                        opacity: transcribeButton.enabled ? 1.0 : 0.5
                    }
                    
                    onClicked: {
                        startTranscription()
                    }
                }
            }
        }
        
        // ==================== PROGRESS SECTION ====================
        Rectangle {
            Layout.fillWidth: true
            height: 80
            color: root.bgCard
            radius: root.borderRadius
            visible: root.currentTaskId.length > 0
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 16
                spacing: 8
                
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    Text {
                        text: "⏳ Processing..."
                        font.pixelSize: 14
                        font.bold: true
                        color: root.accent
                    }
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: root.accent
                        opacity: 0.3
                    }
                }
                
                // Progress Bar
                ProgressBar {
                    id: progressBar
                    Layout.fillWidth: true
                    value: root.currentProgress / 100.0
                    palette.highlight: root.accent
                    
                    background: Rectangle {
                        color: root.primary
                        radius: 4
                        opacity: 0.5
                    }
                }
                
                // Status Message
                Label {
                    text: root.statusMessage
                    font.pixelSize: 12
                    color: root.textSecondary
                    elide: Text.ElideRight
                    Layout.fillWidth: true
                }
            }
        }
        
        // ==================== ANALYZE SECTION ====================
        Rectangle {
            Layout.fillWidth: true
            height: 100
            color: root.bgCard
            radius: root.borderRadius
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 16
                spacing: 12
                
                // Section Header
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    Text {
                        text: "🎯 ANALYZE"
                        font.pixelSize: 16
                        font.bold: true
                        color: root.primary
                    }
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: root.primary
                        opacity: 0.3
                    }
                }
                
                // Analysis Results Placeholder
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 12
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 40
                        color: root.primary
                        radius: 4
                        opacity: 0.5
                        
                        ColumnLayout {
                            anchors.centerIn: parent
                            spacing: 2
                            
                            Label {
                                text: "Key"
                                font.pixelSize: 10
                                color: root.textSecondary
                                anchors.horizontalCenter: parent.horizontalCenter
                            }
                            
                            Label {
                                text: "--"
                                font.pixelSize: 14
                                font.bold: true
                                color: root.accent
                                anchors.horizontalCenter: parent.horizontalCenter
                            }
                        }
                    }
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 40
                        color: root.primary
                        radius: 4
                        opacity: 0.5
                        
                        ColumnLayout {
                            anchors.centerIn: parent
                            spacing: 2
                            
                            Label {
                                text: "Tempo"
                                font.pixelSize: 10
                                color: root.textSecondary
                                anchors.horizontalCenter: parent.horizontalCenter
                            }
                            
                            Label {
                                text: "--"
                                font.pixelSize: 14
                                font.bold: true
                                color: root.accent
                                anchors.horizontalCenter: parent.horizontalCenter
                            }
                        }
                    }
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 40
                        color: root.primary
                        radius: 4
                        opacity: 0.5
                        
                        ColumnLayout {
                            anchors.centerIn: parent
                            spacing: 2
                            
                            Label {
                                text: "Form"
                                font.pixelSize: 10
                                color: root.textSecondary
                                anchors.horizontalCenter: parent.horizontalCenter
                            }
                            
                            Label {
                                text: "--"
                                font.pixelSize: 14
                                font.bold: true
                                color: root.accent
                                anchors.horizontalCenter: parent.horizontalCenter
                            }
                        }
                    }
                }
                
                // Analyze Button
                Button {
                    text: "🔍 Analyze Current Score"
                    Layout.fillWidth: true
                    palette.button: root.primary
                    palette.buttonText: root.textPrimary
                    
                    onClicked: {
                        analyzeCurrentScore()
                    }
                }
            }
        }
        
        // ==================== ARRANGE SECTION ====================
        Rectangle {
            Layout.fillWidth: true
            height: 120
            color: root.bgCard
            radius: root.borderRadius
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 16
                spacing: 12
                
                // Section Header
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    Text {
                        text: "🎨 ARRANGE"
                        font.pixelSize: 16
                        font.bold: true
                        color: root.primary
                    }
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: root.primary
                        opacity: 0.3
                    }
                }
                
                // Style Selector
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    Label {
                        text: "Style:"
                        font.pixelSize: 13
                        color: root.textSecondary
                    }
                    
                    ComboBox {
                        id: styleSelector
                        Layout.fillWidth: true
                        model: ["Jazz Ballad Strings", "Bossa Nova Guitar", "Orchestral Pop", "Rock Band"]
                        palette.button: root.primary
                        palette.buttonText: root.textPrimary
                    }
                }
                
                // Instrument Checkboxes
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    CheckBox {
                        text: "Violin I"
                        checked: true
                        palette.buttonText: root.textSecondary
                        font.pixelSize: 11
                    }
                    
                    CheckBox {
                        text: "Viola"
                        checked: true
                        palette.buttonText: root.textSecondary
                        font.pixelSize: 11
                    }
                    
                    CheckBox {
                        text: "Cello"
                        checked: true
                        palette.buttonText: root.textSecondary
                        font.pixelSize: 11
                    }
                }
                
                // Arrange Button
                Button {
                    text: "✨ Add Arrangement"
                    Layout.fillWidth: true
                    palette.button: root.primary
                    palette.buttonText: root.textPrimary
                    
                    onClicked: {
                        applyArrangement()
                    }
                }
            }
        }
        
        // ==================== SKILL MANAGER SECTION ====================
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            color: root.bgCard
            radius: root.borderRadius
            
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 16
                spacing: 12
                
                // Section Header
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    Text {
                        text: "📝 SKILL MANAGER"
                        font.pixelSize: 16
                        font.bold: true
                        color: root.primary
                    }
                    
                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: root.primary
                        opacity: 0.3
                    }
                }
                
                // Action Buttons
                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8
                    
                    Button {
                        text: "New"
                        Layout.fillWidth: true
                        palette.button: root.primary
                        palette.buttonText: root.textPrimary
                        font.pixelSize: 12
                        
                        onClicked: createNewSkill()
                    }
                    
                    Button {
                        text: "Edit"
                        Layout.fillWidth: true
                        palette.button: root.primary
                        palette.buttonText: root.textPrimary
                        font.pixelSize: 12
                        
                        onClicked: editSelectedSkill()
                    }
                    
                    Button {
                        text: "Compile"
                        Layout.fillWidth: true
                        palette.button: root.accent
                        palette.buttonText: "#000000"
                        font.bold: true
                        font.pixelSize: 12
                        
                        onClicked: compileSelectedSkill()
                    }
                    
                    Button {
                        text: "Delete"
                        Layout.fillWidth: true
                        palette.button: "#c53030"
                        palette.buttonText: root.textPrimary
                        font.pixelSize: 12
                        
                        onClicked: deleteSelectedSkill()
                    }
                }
                
                // Skills List
                ListView {
                    id: skillsList
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    clip: true
                    spacing: 4
                    
                    model: ListModel {
                        ListElement { name: "jazz_ballad_strings"; status: "✓"; instruments: "Violin, Viola, Cello" }
                        ListElement { name: "bossa_nova_guitar"; status: "✓"; instruments: "Nylon Guitar" }
                        ListElement { name: "orchestral_pop"; status: ""; instruments: "Full Orchestra" }
                        ListElement { name: "rock_band"; status: ""; instruments: "Guitar, Bass, Drums" }
                    }
                    
                    delegate: Rectangle {
                        width: skillsList.width
                        height: 50
                        color: index % 2 === 0 ? root.primary : root.bgCard
                        radius: 4
                        opacity: 0.7
                        
                        RowLayout {
                            anchors.fill: parent
                            anchors.margins: 8
                            spacing: 8
                            
                            Text {
                                text: model.status
                                font.pixelSize: 16
                                color: model.status === "✓" ? root.success : root.textSecondary
                            }
                            
                            ColumnLayout {
                                Layout.fillWidth: true
                                spacing: 2
                                
                                Label {
                                    text: model.name.replace(/_/g, " ").toUpperCase()
                                    font.pixelSize: 12
                                    font.bold: true
                                    color: root.textPrimary
                                }
                                
                                Label {
                                    text: model.instruments
                                    font.pixelSize: 10
                                    color: root.textSecondary
                                    elide: Text.ElideRight
                                }
                            }
                        }
                        
                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: skillsList.currentIndex = index
                        }
                    }
                }
            }
        }
    }
    
    // ==================== FUNCTIONS ====================
    
    function checkConnection() {
        // Simulate WebSocket connection check
        root.wsStatus = "Connecting..."
        
        // In production: actual WebSocket connection
        setTimeout(function() {
            root.wsConnected = true
            root.wsStatus = "Connected"
            statusMessage = "Backend connected successfully"
        }, 1000)
    }
    
    function startTranscription() {
        if (urlInput.text.length === 0) {
            return
        }
        
        root.currentTaskId = "txn_" + Math.random().toString(36).substr(2, 8)
        root.currentProgress = 0
        root.statusMessage = "Initializing transcription..."
        
        // Simulate progress updates (Phase 2: replace with real WebSocket events)
        var stages = [
            { stage: "downloading", message: "Downloading audio from source...", progress: 20 },
            { stage: "separating", message: "Isolating instruments using Demucs...", progress: 40 },
            { stage: "transcribing", message: "Converting audio to MIDI with Basic Pitch...", progress: 60 },
            { stage: "quantizing", message: "Cleaning and quantizing rhythm...", progress: 80 },
            { stage: "generating", message: "Generating MusicXML notation...", progress: 100 }
        ]
        
        var stageIndex = 0
        
        function processStage() {
            if (stageIndex < stages.length) {
                var stage = stages[stageIndex]
                root.currentStage = stage.stage
                root.currentProgress = stage.progress
                root.statusMessage = stage.message
                stageIndex++
                setTimeout(processStage, 1500)
            } else {
                // Complete
                setTimeout(function() {
                    root.currentTaskId = ""
                    root.currentProgress = 0
                    root.statusMessage = "Transcription complete! Score opened in MuseScore."
                }, 1000)
            }
        }
        
        processStage()
    }
    
    function analyzeCurrentScore() {
        statusMessage = "Analyzing current score..."
        
        // Simulate analysis (Phase 4: replace with real API call)
        setTimeout(function() {
            statusMessage = "Analysis complete: G Major, 120 BPM, AABA form"
        }, 2000)
    }
    
    function applyArrangement() {
        var selectedStyle = styleSelector.currentText
        statusMessage = "Applying " + selectedStyle + " arrangement..."
        
        // Simulate arrangement (Phase 4: replace with real API call)
        setTimeout(function() {
            statusMessage = "Arrangement applied successfully!"
        }, 2500)
    }
    
    function createNewSkill() {
        statusMessage = "Creating new skill template..."
        // Open skill editor dialog
    }
    
    function editSelectedSkill() {
        if (skillsList.currentIndex >= 0) {
            statusMessage = "Editing skill..."
            // Open skill editor with selected skill
        } else {
            statusMessage = "Please select a skill to edit"
        }
    }
    
    function compileSelectedSkill() {
        if (skillsList.currentIndex >= 0) {
            statusMessage = "Compiling skill with AI..."
            // Call backend /api/skills/compile endpoint
        } else {
            statusMessage = "Please select a skill to compile"
        }
    }
    
    function deleteSelectedSkill() {
        if (skillsList.currentIndex >= 0) {
            statusMessage = "Deleting skill..."
            // Call backend /api/skills/{name} DELETE endpoint
        } else {
            statusMessage = "Please select a skill to delete"
        }
    }
    
    // Auto-connect on startup
    Component.onCompleted: {
        console.log("MaestroPro UI initialized")
        checkConnection()
    }
}
