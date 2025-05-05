from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()



from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    DuckDuckGoSearchTool,
    VisitWebpageTool,
    HfApiModel, 
    LiteLLMModel
)


#model1 =  HfApiModel(model_id="HuggingFaceH4/zephyr-7b-beta")

# model = LiteLLMModel(
#     model_id="meta-llama/Meta-Llama-3-8B-Instruct",
#     api_base="https://api.groq.com/openai/v1",  # Required for Groq
#     api_key=os.getenv("GROQ_API_KEY")           # Picks token from .env
# )

# Using Hugging Face model
# model2 = HfApiModel(
#     model_id="HuggingFaceH4/zephyr-7b-beta"  # Open-access model
# )

# model3 = HfApiModel(model_id="mistralai/Mistral-7B-Instruct-v0.1")

hfModel = HfApiModel(token = os.getenv("HUGGINGFACEHUB_API_TOKEN"))

agent = ToolCallingAgent(
    tools =[DuckDuckGoSearchTool(), VisitWebpageTool()],
    model = hfModel,
    add_base_tools = True
)

prompt = """
        Fetch the share price of google from 2020 to 2024, and create a line graph from it?
        """
# answer = agent.run(prompt)

agent.run(prompt)

# print(answer)