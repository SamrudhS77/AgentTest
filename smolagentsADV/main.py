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

