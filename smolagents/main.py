from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

print("Token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))


from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    DuckDuckGoSearchTool,
    VisitWebpageTool,
    HfApiModel, 
    LiteLLMModel
)


#model1 =  HfApiModel(model_id="HuggingFaceH4/zephyr-7b-beta")

model = LiteLLMModel(
    model_id="meta-llama/Meta-Llama-3-8B-Instruct",
    api_base="https://api.groq.com/openai/v1",  # Required for Groq
    api_key=os.getenv("GROQ_API_KEY")           # Picks token from .env
)

agent = ToolCallingAgent(
    tools =[DuckDuckGoSearchTool(), VisitWebpageTool()],
    model = model1,
    add_base_tools = True
)

answer = agent.run("fetch the share price of google from 2020 to 2024, and create a line graph from it?")

print(answer)