"""
Financial Investment Advisor:

The chain will:

Take a company or stock name as input.
Generate a brief investment summary.
Suggest potential risks.
Recommend a conservative or aggressive strategy.
"""

import time

# Start timer
start_time = time.time()


import os
import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
dotenv.load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)





# Step 1: Investment summary
summary_prompt = PromptTemplate.from_template(
    "Provide a concise investment summary for the company or stock: {company}."
)

# Step 2: Potential risks
risk_prompt = PromptTemplate.from_template(
    "List potential risks or challenges related to investing in {company}."
)

# Step 3: Strategy recommendation
strategy_prompt = PromptTemplate.from_template(
    "Based on the summary and risks, recommend a conservative and an aggressive investment strategy for {company}."
)

print("=== Financial Investment Advisor ===")
print("Type 'exit' to quit\n")

while True:
    company = input("Enter company or stock symbol: ").strip()
    if company.lower() == "exit":
        break

    # Step 1: Summary
    summary_response = llm.invoke(summary_prompt.invoke({"company": company}))

    # Step 2: Risks
    risk_response = llm.invoke(risk_prompt.invoke({"company": company}))

    # Step 3: Strategy
    strategy_response = llm.invoke(strategy_prompt.invoke({"company": company}))

    # Print results
    print("\n--- Investment Summary ---")
    print(summary_response.content)
    print("\n--- Potential Risks ---")
    print(risk_response.content)
    print("\n--- Recommended Strategies ---")
    print(strategy_response.content)
    print("--------------------------------\n")


# Calculate elapsed time
elapsed = end_time - start_time
print(f"Elapsed time: {elapsed:.4f} seconds")