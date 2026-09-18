"""
MaestroPro Skill Compiler
Maya Instruments Technology

Compiles Markdown music theory rules into executable Python code using Ollama.
"""

import httpx
from typing import Optional, Dict, Any
from pathlib import Path
import sys
import importlib.util

from ..config import settings


class SkillCompiler:
    """
    Compiles Markdown-based music theory rules into executable Python classes.
    
    The compiler sends user-written Markdown rules to a local Ollama instance
    running Qwen 2.5 Coder, which generates Python code using music21 to implement
    the specified arrangement rules.
    """
    
    def __init__(self, ollama_host: str = None, ollama_port: int = None, model: str = None):
        """
        Initialize the Skill Compiler.
        
        Args:
            ollama_host: Hostname of the Ollama server
            ollama_port: Port number of the Ollama server
            model: LLM model to use for code generation
        """
        self.ollama_host = ollama_host or settings.ollama_host
        self.ollama_port = ollama_port or settings.ollama_port
        self.model = model or settings.ollama_model
        self.base_url = f"http://{self.ollama_host}:{self.ollama_port}"
        
        # System prompt for generating music21 arrangement code
        self.system_prompt = """You are an expert music theory and Python developer specializing in music21.
Your task is to generate a Python class that implements music arrangement rules based on Markdown input.

GUIDELINES:
1. Create a class named `ArrangementRule` with a method `apply(score)` that takes a music21 Stream
2. Use only music21 library functions for music manipulation
3. Include proper error handling
4. Add docstrings explaining each method
5. Return the modified score from the apply method
6. Do NOT include any imports other than music21
7. Generate clean, production-ready code

EXAMPLE OUTPUT FORMAT:
```python
from music21 import stream, note, chord, key, tempo

class ArrangementRule:
    \"\"\"Implements specific music arrangement rules.\"\"\"
    
    def __init__(self):
        self.rule_name = "Custom Rule"
    
    def apply(self, score: stream.Stream) -> stream.Stream:
        \"\"\"Apply arrangement rules to the score.\"\"\"
        # Implementation here
        return score
```

Generate ONLY the Python code block, nothing else."""

    async def compile_rules(self, markdown_rules: str, rule_name: str = "CustomRule") -> Optional[str]:
        """
        Compile Markdown rules into Python code using Ollama.
        
        Args:
            markdown_rules: User-defined music theory rules in Markdown format
            rule_name: Name for the generated rule class
            
        Returns:
            Generated Python code as a string, or None if compilation fails
        """
        prompt = f"""Create an arrangement rule named '{rule_name}' based on these music theory rules:

{markdown_rules}

Generate the Python class implementation using music21."""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": self.system_prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 2048,
            }
        }

        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload
                )
                response.raise_for_status()
                result = response.json()
                
                # Extract generated code
                generated_code = result.get("response", "")
                
                # Clean up the code (remove markdown code blocks if present)
                generated_code = self._extract_code_block(generated_code)
                
                return generated_code
                
        except httpx.HTTPError as e:
            print(f"HTTP error during skill compilation: {e}")
            return None
        except Exception as e:
            print(f"Error during skill compilation: {e}")
            return None

    def _extract_code_block(self, text: str) -> str:
        """
        Extract Python code from markdown code blocks.
        
        Args:
            text: Text potentially containing markdown code blocks
            
        Returns:
            Extracted code without markdown formatting
        """
        import re
        
        # Pattern to match ```python ... ``` blocks
        pattern = r"```python\s*(.*?)\s*```"
        matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
        
        if matches:
            return matches[0].strip()
        
        # Try generic code block pattern
        pattern_generic = r"```\s*(.*?)\s*```"
        matches_generic = re.findall(pattern_generic, text, re.DOTALL)
        
        if matches_generic:
            return matches_generic[0].strip()
        
        # Return original text if no code blocks found
        return text.strip()

    def save_rule(self, code: str, filename: str, output_dir: str = "./compiled_rules") -> Path:
        """
        Save compiled rule to a Python file.
        
        Args:
            code: Python code to save
            filename: Name of the file (without .py extension)
            output_dir: Directory to save the file
            
        Returns:
            Path to the saved file
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        file_path = output_path / f"{filename}.py"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        
        print(f"Saved compiled rule to: {file_path}")
        return file_path

    def load_rule(self, file_path: Path) -> Optional[Any]:
        """
        Dynamically load a compiled rule from a Python file.
        
        Args:
            file_path: Path to the compiled rule file
            
        Returns:
            Instantiated ArrangementRule class, or None if loading fails
        """
        try:
            # Load module from file
            spec = importlib.util.spec_from_file_location("arrangement_rule", file_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules["arrangement_rule"] = module
            spec.loader.exec_module(module)
            
            # Instantiate the ArrangementRule class
            if hasattr(module, "ArrangementRule"):
                rule_instance = module.ArrangementRule()
                print(f"Successfully loaded rule: {rule_instance.rule_name}")
                return rule_instance
            else:
                print("Error: No ArrangementRule class found in module")
                return None
                
        except Exception as e:
            print(f"Error loading rule: {e}")
            return None

    async def compile_and_load(self, markdown_rules: str, rule_name: str = "CustomRule") -> Optional[Any]:
        """
        Complete pipeline: compile Markdown rules and load the resulting class.
        
        Args:
            markdown_rules: User-defined music theory rules in Markdown format
            rule_name: Name for the generated rule class
            
        Returns:
            Instantiated ArrangementRule class, or None if compilation/loading fails
        """
        # Compile the rules
        code = await self.compile_rules(markdown_rules, rule_name)
        
        if not code:
            print("Failed to compile rules")
            return None
        
        # Save the compiled code
        file_path = self.save_rule(code, rule_name.lower())
        
        # Load and return the rule instance
        rule_instance = self.load_rule(file_path)
        
        return rule_instance


# Convenience function for quick compilation
async def compile_skill(markdown_rules: str, rule_name: str = "CustomRule") -> Optional[Any]:
    """
    Quick helper function to compile and load a skill rule.
    
    Args:
        markdown_rules: Music theory rules in Markdown format
        rule_name: Name for the rule
        
    Returns:
        Instantiated ArrangementRule class or None
    """
    compiler = SkillCompiler()
    return await compiler.compile_and_load(markdown_rules, rule_name)
