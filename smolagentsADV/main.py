from dontenv import load_dotenv
import os

from smolagents import ToolCallingAgent, LiteLLMModel
from tools.python_exec_tool import PythonExecutionTool
from tools.file_loader_tool import FileLoaderTool
from agents.manager_agent import ManagerAgent

load_dotenv()

model = LiteLLMModel(
    model_id= "meta-llama/llama-4-scout-17b-16e-instruct",
    api_base= "https://api.groq.com/openai/v1/models",
    api_key = os.getenv("GROQ_API_KEY")
)

manager_agent = ManagerAgent()

agent = ToolCallingAgent(
    tools=[
        PythonExecutionTool(),
        FileLoaderTool()
    ],
    model = model,
    manager_agent = manager_agent,
    add_base_tools = True
)

prompt = """
You are a data analyst. The dataset is located at './data/sample.csv'.

1. Load the dataset using 'load_csv'.
2. Use data exploration agent to summarize and inspect it.
3. Use data cleaning agent to clean missing data, fix types, and remove duplicates.
4. Then, use 'python_executor' to generate histograms for numeric columns.
"""

agent.run(prompt)