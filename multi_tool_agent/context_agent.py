# agent.py
import os
import json
from typing import List, Dict
from google.adk.agents import Agent
from context_data import EXPORTS_CONTEXT, format_exports_context
from file_context import EXISTING_FILE_CODE, file_context_str
from google.adk.agents.readonly_context import ReadonlyContext

# This is an InstructionProvider
def my_instruction_provider(context: ReadonlyContext, goal: str) -> str:
    return f"""
You are the CONTEXT AGENT. Your job is to prepare all relevant information
for the CODE GENERATOR agent.

The user's GOAL is:

{goal}

========================
Available Project Exports
========================
{format_exports_context(EXPORTS_CONTEXT)}

========================
Existing File Context
========================
{file_context_str(EXISTING_FILE_CODE)}

========================
Instruction
========================
1. Combine the GOAL, Project Exports, and File Context into a structured,
   well-organized prompt that a code generator can directly use.
2. Do not generate code yourself.
3. Ensure clarity, proper formatting, and completeness.
"""

# -------------------------------
# Define the Context Agent
# -------------------------------
context_agent = Agent(
    name="context_agent",
    model=os.getenv("MODEL_ID", "gemini-2.0-flash"),  # flash is faster for prep
    description="Collects GOAL, project exports, and file context, then prepares a complete structured prompt for the code generator.",
    instruction=my_instruction_provider,
)