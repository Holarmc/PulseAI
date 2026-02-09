from google.adk.agents.llm_agent import Agent
from src.tools.civic_tools import record_civic_issue
from src.utils.yaml_loader import load_config, load_instructions
from google.adk.tools import AgentTool


class PulseCoordinator:
    def __init__(self):
        self.config = load_config("configs/agent_config.yaml")
        
        # 1. Initialize Specialized Agents
        self.works_agent = Agent(
            model=self.config['ministries']['works']['model'],
            name=self.config['ministries']['works']['name'],
            instruction=load_instructions(self.config['ministries']['works']['instruction_path']),
            tools=[record_civic_issue]
        )

        self.water_agent = Agent(
            model=self.config['ministries']['water']['model'],
            name=self.config['ministries']['water']['name'],
            instruction=load_instructions(self.config['ministries']['water']['instruction_path']),
            tools=[record_civic_issue]
        )

        # 2. Initialize the Root/Router Agent
        self.root_agent = Agent(
            model=self.config['coordinator']['model'],
            name=self.config['coordinator']['name'],
            instruction=load_instructions(self.config['coordinator']['instruction_path']),
            tools=[AgentTool(self.works_agent), AgentTool(self.water_agent)] # Routing Pattern
        )

    def get_agent(self):
        return self.root_agent