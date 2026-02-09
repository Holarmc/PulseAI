# from src.agents.coordinator_agent import PulseCoordinator
# import asyncio
# from google.adk.runners import InMemoryRunner

# async def main():
#     system = PulseCoordinator()
#     agent = system.get_agent()

#     print("Kwara PulseAI [Terminal Mode]")
#     while True:
#         user_input = input("[user]: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
        
#         # This is the programmatic way to call the agent
#         # without the ADK CLI wrapper
#         # response = agent.run(user_input)
#         # print(f"[PulseAI]: {response}")
#         runner = InMemoryRunner(agent=agent)
#         response = await runner.run_debug(
#             user_input
#         )
#         print(response)

# if __name__ == "__main__":
#     asyncio.run(main())