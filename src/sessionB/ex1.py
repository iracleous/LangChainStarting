"""

Fully interactive LangChain demo using the Runnable API, 
where the user types topics and the chain generates:

A simple explanation
A fun fact
All in one composable pipeline.

"""

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 1️⃣ Prompt for a simple explanation
explain_prompt = PromptTemplate.from_template(
    "Explain {topic} in a simple way suitable for a 10-year-old."
)

# 2️⃣ Prompt for a fun fact
fun_fact_prompt = PromptTemplate.from_template(
    "Now provide a fun and surprising fact about {topic}."
)

# 3️⃣ Initialize the LLM
import os
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL"),  # default to gpt-4o
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0
    )


# 4️⃣ Build a composable Runnable pipeline
# explanation → fun fact
chain = explain_prompt | llm | fun_fact_prompt | llm

print("Interactive Explanation + Fun Fact (type 'exit' to quit)\n")

# 5️⃣ Interactive loop
while True:
    topic = input("Enter a topic: ")
    if topic.strip().lower() == "exit":
        break

    # Run the pipeline
    response = chain.invoke({"topic": topic})

    # Print the structured response
    print("\n--- Generated Output ---")
    print(response.content)
    print("------------------------\n")
