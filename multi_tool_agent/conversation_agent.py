import os
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from dotenv import load_dotenv
from context_data import EXPORTS_CONTEXT,All_SCHEMAS, format_exports_context,format_schema_context
from file_context import EXISTING_FILE_CODE, file_context_str
import os
from google.adk.agents.readonly_context import ReadonlyContext

load_dotenv()


def my_instruction_provider(context: ReadonlyContext) -> str:
    return f"""
You are a helpful software project assistant.

1. You will be provided with:
   - Available project exports (API, utilities, components, services, etc.)
   - Existing file context (the code of a specific file)

2. Your task is:
   - Do NOT ask the user any clarifying questions.
   - Directly analyze the context and provide a **final GOAL** in a structured format.


3. The output format must strictly follow this template:

FINAL_PROMPT:
========================
Available Project Exports
========================
{format_exports_context(EXPORTS_CONTEXT)}
========================
All Schemas for Project
===========================
{format_schema_context(All_SCHEMAS)}

========================
Existing File Context
========================
{file_context_str(EXISTING_FILE_CODE)}

========================
GOAL
========================
- Clear description of the feature or change
- Any functional requirements
- Any design/UX considerations
- Any validation/business rules

⚠️ Rules:
- Do NOT generate or suggest code.
- Only summarize and refine the final GOAL based on the user’s intent.
- Keep the GOAL concise but precise.
- Do not add context in the goal just a proper promt
- Do not ask any question
"""


conversation_agent = Agent(
    name="conversation_agent",
    model=os.getenv("MODEL_ID", "gemini-2.0-flash"),
    description="Talks to the user, clarifies their goal, and outputs a refined GOAL for code generation for a particular file considering the context in mind.",
    instruction=my_instruction_provider
)
