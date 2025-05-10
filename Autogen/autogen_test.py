import autogen
import os
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

config_list = [
    {
        "model": "llama3-70b-8192",
        "api_key": os.getenv("GROQ_API_KEY"),
        "base_url": "https://api.groq.com/openai/v1"
    }
]

""""
Basic Autogen set up to understand how a writer agent and an editor agent can work together, using a user proxy.
"""


writer_agent = autogen.AssistantAgent(
    name="writer",
    llm_config= {"config_list": config_list,
                 "temperature": 0.8}
)

editor_agent = autogen.AssistantAgent(
    name="editor",
    llm_config= {"config_list": config_list,
                 "temperature": 0.0}
)

user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config=False
)
