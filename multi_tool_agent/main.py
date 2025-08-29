# # agent.py (main entrypoint)

# from conversation_agent import conversation_agent
# from context_agent import context_agent
# from agent import code_generator_agent

# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.genai import types
# import asyncio

# session_service = InMemorySessionService()

# conversation_runner = Runner(
#     agent=conversation_agent,
#     app_name="File Modifier",
#     session_service=session_service
# )

# APP_NAME = "weather_app"
# USER_ID = "user_123"
# SESSION_ID = "session_456"


# def run_query(query):

#     content = types.Content(
#         role="user",
#         parts=[types.Part(text=query)]
#     )
#     # Run the agent with the runner
#     events = conversation_runner.run(
#         user_id=USER_ID,
#         session_id=SESSION_ID,
#         new_message=content
#     )
#     # Process events to get the final response
#     for event in events:
#         if event.is_final_response():
#             return event.content.parts[0].text
#     return "No response received."
# # Example of usage


# async def run_system(user_input: str):

#     # Create session service and session

#     session = await session_service.create_session(
#         app_name=APP_NAME,
#         user_id=USER_ID,
#         session_id=SESSION_ID
#     )
#     # Step 1: Conversation agent interprets user request
#     response = run_query("Get me the code using login ")

#     print("Conversation Agent:", response)
#     return "done"
#     # # Step 2: Context agent prepares/retrieves project context
#     # context = context_agent.run(conversation_response)
#     # print("Context Agent:", context)

#     # # Step 3: Code generator agent creates output
#     # codegen_response = code_generator_agent.run(context)
#     # print("Codegen Agent:", codegen_response)

#     # return codegen_response


# if __name__ == "__main__":
#     result = asyncio.run(run_system("Create a Flask app with /hello endpoint"))
#     print("\nFinal Result:", result)


# agent.py (main entrypoint)
##################################################
# import asyncio
# from conversation_agent import conversation_agent
# from agent import code_generator_agent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.genai import types

# APP_NAME = "File Modifier"
# USER_ID = "user_123"
# SESSION_ID = "session_456"


# async def run_system(user_input: str):
#     # Create session service
#     session_service = InMemorySessionService()

#     # Create session BEFORE calling the runner
#     await session_service.create_session(
#         app_name=APP_NAME,
#         user_id=USER_ID,
#         session_id=SESSION_ID
#     )

#     # Create the runner
#     conversation_runner = Runner(
#         agent=conversation_agent,
#         app_name=APP_NAME,
#         session_service=session_service
#     )

#     # Wrap the user input in types.Content
#     content = types.Content(
#         role="user",
#         parts=[types.Part(text=user_input)]
#     )

#     # Run the agent
#     events = conversation_runner.run(
#         user_id=USER_ID,
#         session_id=SESSION_ID,
#         new_message=content
#     )

#     # Get final response
#     for event in events:
#         if event.is_final_response():
#             print("Conversation Agent:", event.content.parts[0].text)
#             return event.content.parts[0].text

#     return "No response received."

# if __name__ == "__main__":

#     # async def main():
#     #     print("Start talking to the agent. Type 'exit' to quit.")
#     #     while True:
#     #         user_input = input("You: ")
#     #         if user_input.lower() == "exit":
#     #             break

#     #         # Send the message to conversation_agent in the same session
#     #         response = await run_system(user_input)
#     #         print("Agent:", response)
#     async def conversation_flow(user_input):
#         result = await run_system(user_input)  # Conversation agent logic
#         if "GOAL" in result:   # means clarifications are done
#             return result, True  # (final prompt, finished)
#         return result, False     # (reply, still clarifying)

#     async def codegen_flow(final_prompt):
#         # Create a new session for codegen (you can also reuse the same session_service if you want continuity)
#         session_service = InMemorySessionService()
#         await session_service.create_session(
#             app_name="CodeGen",
#             user_id=USER_ID,
#             session_id="codegen_session_123"
#         )

#         # Create a runner for the codegen agent
#         codegen_runner = Runner(
#             agent=code_generator_agent,
#             app_name="CodeGen",
#             session_service=session_service
#         )

#         # Wrap the final prompt
#         content = types.Content(
#             role="user",
#             parts=[types.Part(text=final_prompt)]
#         )

#         # Run the codegen agent
#         events = codegen_runner.run(
#             user_id=USER_ID,
#             session_id="codegen_session_123",
#             new_message=content
#         )

#         # Collect final response
#         for event in events:
#             if event.is_final_response():
#                 return event.content.parts[0].text

#         return "Codegen produced no response."

#     async def main():
#         print("Start talking to the agent. Type 'exit' to quit.")

#         final_prompt = None

#         while True:
#             user_input = input("You: ")
#             if user_input.lower() == "exit":
#                 break

#             if not final_prompt:
#                 response, is_final = await conversation_flow(user_input)
#                 print("Agent:", is_final)

#                 if is_final:
#                     final_prompt = response  # store final GOAL
#                     print("\n--- Sending final GOAL to CodeGen Tool ---\n")
#                     code_result = await codegen_flow(final_prompt)
#                     print("CodeGen Result:\n", code_result)
#                     break

#     asyncio.run(main())
##########################################################
# import asyncio
# from conversation_agent import conversation_agent
# from agent import code_generator_agent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.genai import types

# APP_NAME = "File Modifier"
# USER_ID = "user_123"
# SESSION_ID = "conversation_session"

# CODEGEN_SESSION_ID = "codegen_session_123"


# async def send_to_agent(agent, session_service, session_id, message):
#     """Send a message to an agent and return the final response."""
#     runner = Runner(agent=agent, app_name=APP_NAME,
#                     session_service=session_service)
#     content = types.Content(role="user", parts=[types.Part(text=message)])
#     events = runner.run(
#         user_id=USER_ID, session_id=session_id, new_message=content)

#     for event in events:
#         if event.is_final_response():
#             return event.content.parts[0].text
#     return None


# async def main():
#     # Create persistent sessions (one for conv, one for codegen)
#     session_service_conv = InMemorySessionService()
#     session_service_codegen = InMemorySessionService()

#     await session_service_conv.create_session(app_name=APP_NAME,
#                                               user_id=USER_ID,
#                                               session_id=SESSION_ID)
#     await session_service_codegen.create_session(app_name=APP_NAME,
#                                                  user_id=USER_ID,
#                                                  session_id=CODEGEN_SESSION_ID)

#     print("Agent will start the conversation...")

#     user_input = None
#     final_prompt = None

#     while True:
#         # -------- Clarification Loop --------
#         while True:
#             agent_response = await send_to_agent(
#                 conversation_agent,
#                 session_service_conv,
#                 SESSION_ID,
#                 f"User says: '{user_input}'"
#                 if user_input
#                 else "Start the conversation and ask what the user wants to create. "
#                      "Ask clarifying questions as needed. When ready, produce the final prompt "
#                      "for code generation using FINAL_PROMPT: "
#             )
#             print("Agent:", agent_response)

#             if "FINAL_PROMPT:" in agent_response:
#                 final_prompt = agent_response.replace(
#                     "FINAL_PROMPT:", "").strip()
#                 break
#             else:
#                 user_input = input("You: ")

#         # -------- CodeGen Loop --------
#         code_result = await send_to_agent(
#             code_generator_agent,
#             session_service_codegen,
#             CODEGEN_SESSION_ID,
#             final_prompt
#         )
#         print("\nCodeGen Result:\n", code_result)

#         # Accept / Reject flow
#         print("Agent: Do you accept this code or reject it?")
#         user_choice = input("You (Accept/Reject): ").strip().lower()

#         if user_choice == "accept":
#             print("✅ Code accepted. Flow finished.")
#             break
#         else:
#             user_input = input("Provide a revised description or prompt: ")
#             final_prompt = None  # reset so clarification loop starts again

# asyncio.run(main())

import asyncio
from conversation_agent import conversation_agent
from agent import code_generator_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

APP_NAME = "File Modifier"
USER_ID = "user_123"
SESSION_ID = "conversation_session"
CODEGEN_SESSION_ID = "codegen_session_123"


# Abstracting the Agent interaction into a reusable class
class AgentRunner:
    def __init__(self, app_name: str, session_service: InMemorySessionService):
        self.app_name = app_name
        self.session_service = session_service

    async def send_message(self, agent, session_id: str, user_id: str, message: str) -> str:
        """Sends a message to an agent and returns the final response."""
        runner = Runner(agent=agent, app_name=self.app_name, session_service=self.session_service)
        content = types.Content(role="user", parts=[types.Part(text=message)])
        events = runner.run(user_id=user_id, session_id=session_id, new_message=content)

        for event in events:
            if event.is_final_response():
                return event.content.parts[0].text
        return None


# Abstracting the entire application logic into a class
class AppOrchestrator:
    def __init__(self, app_name: str, user_id: str):
        self.app_name = app_name
        self.user_id = user_id
        self.session_service_conv = InMemorySessionService()
        self.session_service_codegen = InMemorySessionService()
        self.agent_runner = AgentRunner(app_name, self.session_service_conv)
        self.agent_runner_codegen = AgentRunner(app_name, self.session_service_codegen)
        self.conversation_agent = conversation_agent
        self.code_generator_agent = code_generator_agent
        self.session_id = SESSION_ID
        self.codegen_session_id = CODEGEN_SESSION_ID

    async def setup_sessions(self):
        """Initializes the persistent sessions for the agents."""
        await self.session_service_conv.create_session(
            app_name=self.app_name, user_id=self.user_id, session_id=self.session_id
        )
        await self.session_service_codegen.create_session(
            app_name=self.app_name, user_id=self.user_id, session_id=self.codegen_session_id
        )

    async def run(self):
        """Executes the main application logic and orchestrates the agent flow."""
        await self.setup_sessions()
        print("Agent will start the conversation...")
        user_input = None
        final_prompt = None

        while True:
            # -------- Clarification Loop --------
            while True:
                agent_response = await self.agent_runner.send_message(
                    self.conversation_agent,
                    self.session_id,
                    self.user_id,
                    f"User says: '{user_input}'"
                    if user_input
                    else "Start the conversation and ask what the user wants to create. "
                         "Ask clarifying questions as needed. When ready, produce the final prompt "
                         "for code generation using  FINAL_PROMPT: ",
                )
                print("Agent:", agent_response)

                if "FINAL_PROMPT:" in agent_response:
                    final_prompt = agent_response.replace("FINAL_PROMPT:", "").strip()
                    break
                else:
                    user_input = input("You: ")

            # -------- CodeGen Loop --------
            code_result = await self.agent_runner_codegen.send_message(
                self.code_generator_agent,
                self.codegen_session_id,
                self.user_id,
                final_prompt,
            )
            print("\nCodeGen Result:\n", code_result)

            # Accept / Reject flow
            print("Agent: Do you accept this code or reject it?")
            user_choice = input("You (Accept/Reject): ").strip().lower()

            if user_choice == "accept":
                print("✅ Code accepted. Flow finished.")
                break
            else:
                user_input = input("Provide a revised description or prompt: ")
                final_prompt = None  # reset so clarification loop starts again


async def main():
    orchestrator = AppOrchestrator(APP_NAME, USER_ID)
    await orchestrator.run()


if __name__ == "__main__":
    asyncio.run(main())
