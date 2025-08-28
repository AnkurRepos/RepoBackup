# agent.py
import os
import json
from typing import List, Dict
from google.adk.agents import Agent
# from .context_data import EXPORTS_CONTEXT, format_exports_context
# from .file_context import EXISTING_FILE_CODE, file_context_str
from google.adk.agents.readonly_context import ReadonlyContext

# This is an InstructionProvider


def my_instruction_provider(context: ReadonlyContext) -> str:
    # You can optionally use the context to build the instruction
    # For this example, we'll return a static string with literal braces.
    """
    Returns the instruction string for the agent.
    Using a function avoids ADK injecting state into {…}.
    """
    return """
You are a senior software engineer and code generator.

You will be provided:
1. The GOAL: what the user wants to achieve.
2. The CONTEXT: code of the file to modify.
3. Available project exports: functions, hooks, components, variables.
4. Schemas for the project : all schemas that can be used to design variables 

Your process is:
1.  Carefully analyze the user's GOAL and the provided CONTEXT code.
2.  Determine the necessary code changes or new file content.
3.  **Use the `write_files_to_disk` tool to save the new or updated file(s).** The tool expects a list of file objects, where each object has a "path" and a "content".

Rules:
- Ignore standard React/JS built-ins (useState, useEffect, console, Math, etc.)
- Do not change the code if it does not affect the new code 
- Always check if a requested function/component/variable exists in the EXPORTS_CONTEXT before creating a new one.
- Do not remove unrelated code in the existing file.
- Ensure all necessary imports are present.
- **Ignore standard React/JS built-ins** (like `useEffect`, `useState`) if they appear in the code.


"""

# -------------------------------
# Helper: print files to console
# -------------------------------


def print_files_to_console(files: List[Dict[str, str]]) -> None:
    for f in files:
        path = f.get("path", "unnamed.txt")
        content = f.get("content", "")
        print(f"\n===== FILE: {path} =====")
        print(content.rstrip("\n"))
        print(f"===== END FILE: {path} =====")


def write_files_to_disk(files: List[Dict[str, str]], base_dir: str = ".") -> None:
    for f in files:
        path = f.get("path", "unnamed.js")
        content = f.get("content", "")
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(content.rstrip("\n"))
        print(f"✅ Written file: {full_path}")


# -------------------------------
# Define the ADK agent
# -------------------------------
code_generator_agent = Agent(
    name="react_file_modifier",
    model=os.getenv("MODEL_ID", "gemini-2.0-flash"),
    description="Modifies existing code files or injects new code based on project context.",
    tools=[print_files_to_console, write_files_to_disk],

    instruction=my_instruction_provider
)


# Available Project exports:
# {format_exports_context(EXPORTS_CONTEXT)}

# CONTEXT:
# {file_context_str(EXISTING_FILE_CODE)}
