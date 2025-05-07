from smolagents import ManagedAgent
from agents.data_cleaning_agent import DataCleaningAgent
from agents.data_exploration_agent import DataExplorationAgent

class ManagerAgent(ManagedAgent):
    description =  "Orchestrates data exploration and cleaning tasks using sub-agents."

    def run(self, context: str) -> str:
        
        explorer = DataExplorationAgent()
        cleaner = DataCleaningAgent()

        exploration_result = explorer.run(context)

        cleaning_result = cleaner.run(context)

        return f""" DATA EXPLORATION RESULT: \n{exploration_result} 
                    DATA CLEANING RESULT : \n{cleaning_result}
                """
