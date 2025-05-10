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


story_prompt = ("Please write a short story about a bank heist, Oceans 11 style, which takes place in a casino on Mars.")
story = user_proxy.initiate_chat(
    writer_agent,
    message=story_prompt,
    max_turns=1
)

feedback_prompt = ("Please review the following story and provide constructive feedback along with the suggestions for improvements: "+(story))
feedback = user_proxy.initiate_chat(
    editor_agent,
    message=feedback_prompt,
    max_turns=1
)