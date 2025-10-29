"""
"""

from langchain_openai import ChatOpenAI
 
# 1. Initialize the LLM
import os
import dotenv
dotenv.load_dotenv()

# Initialize model
llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL"),  # default to gpt-4o
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0
    )
# 2. use LangChain client to create a simple chain

from langchain_core.prompts import PromptTemplate
# Prompt template
prompt = PromptTemplate.from_template("Explain {topic} in a fun and simple way.")

 

# Runnable pipeline
chain = prompt | llm  # "pipe" operator combines Runnable objects

# Invoke the chain
response = chain.invoke({"topic": "black holes"})
print(response.content)    