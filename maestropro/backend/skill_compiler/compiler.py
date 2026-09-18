"""
MaestroPro - Skill Compiler Core Module
Maya Instruments Technology
Version: 1.0.0

Handles the complete pipeline for compiling Markdown music theory rules
into executable Python classes using Ollama and Qwen 2.5 Coder.

Pipeline:
1. Parse Markdown to extract structured rules
2. Build system prompt with context
3. Send to Ollama API for code generation
4. Validate generated Python syntax (AST)
5. Test in sandbox environment
6. Save compiled .py file and update metadata
7. Dynamically load class for immediate use
"""

import asyncio
import json
import re
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
import logging

from backend.config import settings

logger = logging.getLogger(__name__)


class SkillCompiler:
    """
    Compiles Markdown music theory rules into executable Python arrangement classes.
    
    Usage:
        compiler = SkillCompiler()
        result = await compiler.compile_and_load("jazz_ballad", markdown_content)
        
        if result["success"]:
            arranger_class = result["class"]
            arranger = arranger_class(instruments=["Violin", "Viola", "Cello"])
    """
    
    # System prompt that guides Qwen 2.5 Coder
    SYSTEM_PROMPT = """You are the core AI engine of MaestroPro by Maya Instruments Technology. 
Your task is to convert Markdown music theory rules into a valid, executable 
Python class using the 'music21' library.

STRICT RULES:
1. Output ONLY valid Python code. No markdown formatting, no explanations, 
   no comments outside the code.
2. Class name must be PascalCase matching the style name.
3. Always include these imports at the top:
   from music21 import stream, note, chord, interval, key, meter, pitch
4. Class must include these methods:
   - __init__(self, instruments: list)
   - harmonize(self, chord_progression: list) -> list
   - voice_lead(self, chords: list, instruments: list) -> stream.Score
   - validate_range(self, part: stream.Part, instrument: str) -> bool
5. Use try-except blocks around ALL music21 operations.
6. Implement ALL rules from the Markdown. No placeholders like "pass" or 
   "# TODO" or "# add logic here".
7. If a rule cannot be perfectly implemented in music21, use the closest 
   equivalent and add a Python comment explaining the approximation.
8. Respect physical instrument ranges:
   - Violin: G3 to E7
   - Viola: C3 to A6
   - Cello: C2 to A5
   - Bass: E1 to G4
   - Trumpet: F#3 to D6
   - Trombone: E2 to F5
9. Return only the class definition. No test code, no example usage.
"""
    
    def __init__(self):
        self.ollama_url = settings.OLLAMA_URL
        self.model = settings.DEFAULT_MODEL
        self.temperature = settings.TEMPERATURE
        self.top_p = settings.TOP_P
        self.num_predict = settings.NUM_PREDICT
        self.num_ctx = settings.NUM_CTX
        self.keep_alive = settings.KEEP_ALIVE
    
    async def compile_and_load(
        self,
        name: str,
        markdown_content: str
    ) -> Dict[str, Any]:
        """
        Complete compilation pipeline: parse → generate → validate → save → load.
        
        Args:
            name: Name of the skill/style (e.g., "jazz_ballad")
            markdown_content: Raw Markdown content with music theory rules
        
        Returns:
            Dict with keys:
                - success: bool
                - file_path: str (path to saved .py file)
                - class_name: str (PascalCase class name)
                - class: type (dynamically loaded class)
                - error: str (if success is False)
        """
        logger.info(f"Starting compilation for skill: {name}")
        
        # Step 1: Parse Markdown to extract structured data
        parsed_rules = self._parse_markdown(markdown_content)
        logger.debug(f"Parsed rules: {list(parsed_rules.keys())}")
        
        # Step 2: Build full prompt
        full_prompt = self._build_prompt(name, parsed_rules, markdown_content)
        
        # Step 3: Generate Python code via Ollama
        generated_code = await self._generate_code(full_prompt)
        
        if not generated_code:
            return {
                "success": False,
                "error": "Failed to generate code from Ollama"
            }
        
        logger.debug(f"Generated code length: {len(generated_code)} chars")
        
        # Step 4: Extract clean Python code (remove markdown fences if present)
        clean_code = self._extract_code(generated_code)
        
        # Step 5: Validate syntax with AST
        syntax_valid, syntax_error = self._validate_syntax(clean_code)
        
        if not syntax_valid:
            return {
                "success": False,
                "error": f"Syntax error: {syntax_error}"
            }
        
        logger.info("Syntax validation passed")
        
        # Step 6: Validate imports
        imports_valid, imports_error = self._validate_imports(clean_code)
        
        if not imports_valid:
            return {
                "success": False,
                "error": f"Import error: {imports_error}"
            }
        
        logger.info("Import validation passed")
        
        # Step 7: Sandbox test (optional - test on minimal data)
        # For now, skip sandbox testing to speed up compilation
        # Can be added in Phase 3
        
        # Step 8: Save to file
        file_path = self._save_skill(name, clean_code)
        logger.info(f"Saved skill to: {file_path}")
        
        # Step 9: Update metadata
        self._update_metadata(name, parsed_rules)
        
        # Step 10: Dynamically load class
        try:
            arranger_class = self._load_class(file_path, name)
            class_name = arranger_class.__name__
            
            return {
                "success": True,
                "file_path": str(file_path),
                "class_name": class_name,
                "class": arranger_class,
                "code": clean_code
            }
        except Exception as e:
            logger.error(f"Failed to load class: {e}")
            return {
                "success": False,
                "error": f"Failed to load class: {str(e)}",
                "file_path": str(file_path)
            }
    
    def _parse_markdown(self, markdown_content: str) -> Dict[str, Any]:
        """
        Extract structured rules from Markdown content.
        
        Expected sections:
        - # Style: [Name]
        - ## Target Instruments
        - ## Harmony Rules
        - ## Voice Leading Rules
        - ## Rhythmic Patterns
        - ## Range Constraints
        - ## Special Instructions
        """
        rules = {
            "style_name": "",
            "instruments": [],
            "harmony_rules": [],
            "voice_leading_rules": [],
            "rhythmic_patterns": [],
            "range_constraints": {},
            "special_instructions": []
        }
        
        lines = markdown_content.split("\n")
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Detect headers
            if line.startswith("# Style:"):
                rules["style_name"] = line.replace("# Style:", "").strip()
            elif line.startswith("## Target Instruments"):
                current_section = "instruments"
            elif line.startswith("## Harmony Rules"):
                current_section = "harmony_rules"
            elif line.startswith("## Voice Leading Rules"):
                current_section = "voice_leading_rules"
            elif line.startswith("## Rhythmic Patterns"):
                current_section = "rhythmic_patterns"
            elif line.startswith("## Range Constraints"):
                current_section = "range_constraints"
            elif line.startswith("## Special Instructions"):
                current_section = "special_instructions"
            elif line.startswith("-"):
                # List item
                item = line[1:].strip()
                if current_section == "instruments":
                    rules["instruments"].append(item)
                elif current_section == "harmony_rules":
                    rules["harmony_rules"].append(item)
                elif current_section == "voice_leading_rules":
                    rules["voice_leading_rules"].append(item)
                elif current_section == "rhythmic_patterns":
                    rules["rhythmic_patterns"].append(item)
                elif current_section == "special_instructions":
                    rules["special_instructions"].append(item)
        
        # Use filename as fallback for style name
        if not rules["style_name"]:
            rules["style_name"] = "Unnamed Style"
        
        return rules
    
    def _build_prompt(
        self,
        name: str,
        parsed_rules: Dict[str, Any],
        original_markdown: str
    ) -> str:
        """
        Construct the full prompt to send to Ollama.
        Combines system prompt with user-specific rules.
        """
        class_name = name.replace("_", " ").title().replace(" ", "")
        
        prompt = f"""{self.SYSTEM_PROMPT}

STYLE NAME: {parsed_rules['style_name']}
CLASS NAME: {class_name}

MARKDOWN RULES:
{original_markdown}

Generate the Python class now. Remember: ONLY code, no explanations."""
        
        return prompt
    
    async def _generate_code(self, prompt: str) -> Optional[str]:
        """
        Send prompt to Ollama API and retrieve generated Python code.
        """
        try:
            import httpx
            
            payload = {
                "model": self.model,
                "prompt": prompt,
                "temperature": self.temperature,
                "top_p": self.top_p,
                "num_predict": self.num_predict,
                "num_ctx": self.num_ctx,
                "stream": False,
                "keep_alive": self.keep_alive
            }
            
            logger.info(f"Sending request to Ollama ({self.model})...")
            
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(
                    f"{self.ollama_url}/api/generate",
                    json=payload
                )
                
                if response.status_code == 200:
                    data = response.json()
                    generated_text = data.get("response", "")
                    logger.info("Code generation successful")
                    return generated_text
                else:
                    logger.error(f"Ollama API error: {response.status_code} - {response.text}")
                    return None
        
        except Exception as e:
            logger.error(f"Ollama request failed: {e}")
            return None
    
    def _extract_code(self, raw_response: str) -> str:
        """
        Extract clean Python code from raw LLM response.
        Removes markdown code fences if present.
        """
        # Remove ```python ... ``` blocks
        code_block_pattern = r"```python\s*(.*?)\s*```"
        match = re.search(code_block_pattern, raw_response, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        
        # Remove generic ``` ... ``` blocks
        generic_pattern = r"```\s*(.*?)\s*```"
        match = re.search(generic_pattern, raw_response, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        
        # Return as-is if no fences found
        return raw_response.strip()
    
    def _validate_syntax(self, code: str) -> Tuple[bool, Optional[str]]:
        """
        Validate Python syntax using ast.parse().
        Returns (is_valid, error_message).
        """
        import ast
        
        try:
            ast.parse(code)
            return True, None
        except SyntaxError as e:
            error_msg = f"Syntax Error at line {e.lineno}: {e.msg}"
            logger.error(error_msg)
            return False, error_msg
    
    def _validate_imports(self, code: str) -> Tuple[bool, Optional[str]]:
        """
        Ensure code only imports allowed modules.
        Returns (is_valid, error_message).
        """
        import ast
        
        try:
            tree = ast.parse(code)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        module_name = alias.name.split(".")[0]
                        if module_name not in settings.ALLOWED_IMPORTS:
                            error_msg = f"Disallowed import: {alias.name}"
                            logger.error(error_msg)
                            return False, error_msg
                
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        module_name = node.module.split(".")[0]
                        if module_name not in settings.ALLOWED_IMPORTS:
                            error_msg = f"Disallowed import: {node.module}"
                            logger.error(error_msg)
                            return False, error_msg
            
            return True, None
        
        except Exception as e:
            error_msg = f"Import validation error: {str(e)}"
            logger.error(error_msg)
            return False, error_msg
    
    def _save_skill(self, name: str, code: str) -> Path:
        """
        Save compiled Python code to skills directory.
        """
        file_path = settings.SKILLS_PY_DIR / f"{name}.py"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        
        return file_path
    
    def _update_metadata(self, name: str, parsed_rules: Dict[str, Any]):
        """
        Update skills metadata JSON index.
        """
        metadata_file = settings.metadata_file
        
        # Load existing metadata
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
        else:
            metadata = {"skills": [], "last_updated": ""}
        
        # Create skill entry
        skill_entry = {
            "name": name,
            "style_name": parsed_rules["style_name"],
            "instruments": parsed_rules["instruments"],
            "file": f"{name}.py",
            "status": "compiled",
            "created_at": str(Path(settings.SKILLS_PY_DIR / f"{name}.py").stat().st_mtime)
        }
        
        # Update or add skill
        skills = metadata["skills"]
        existing_index = next((i for i, s in enumerate(skills) if s["name"] == name), None)
        
        if existing_index is not None:
            skills[existing_index] = skill_entry
        else:
            skills.append(skill_entry)
        
        # Save updated metadata
        import datetime
        metadata["last_updated"] = datetime.datetime.now().isoformat()
        
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def _load_class(self, file_path: Path, skill_name: str) -> type:
        """
        Dynamically load Python class from compiled skill file.
        """
        import importlib.util
        import sys
        
        module_name = f"maestropro_skill_{skill_name}"
        
        # Check if module already loaded
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        
        if spec is None or spec.loader is None:
            raise ImportError(f"Failed to load module spec from {file_path}")
        
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        # Find the class (PascalCase version of skill_name)
        class_name = skill_name.replace("_", " ").title().replace(" ", "")
        
        arranger_class = getattr(module, class_name, None)
        
        if arranger_class is None:
            # Fallback: find first class in module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and attr_name != "object":
                    arranger_class = attr
                    break
        
        if arranger_class is None:
            raise ValueError(f"No class found in {file_path}")
        
        logger.info(f"Loaded class: {arranger_class.__name__}")
        
        return arranger_class
