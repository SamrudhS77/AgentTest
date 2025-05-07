from dontenv import load_dotenv
import os

from smolagents import ToolCallingAgent, LiteLLMModel
from tools.python_exec_tool import PythonExecutionTool
from tools.file_loader_tool import FileLoaderTool