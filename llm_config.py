import os
from dotenv import load_dotenv
from crewai import LLM
from openai import AzureOpenAI

load_dotenv()

llm = LLM(
    model="azure/gpt-4o",
    temperature=0.5,
    api_key=os.getenv("AZURE_API"),
    base_url=os.getenv("AZURE_ENDPOINT"),
    api_version=os.getenv("API_VERSION")
)