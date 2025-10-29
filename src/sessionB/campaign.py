"""
“Marketing Campaign Advisor”:

Step 1: Generate a campaign idea for a given product.
Step 2: Suggest an attention-grabbing tagline.
Step 3: Give a risk/mitigation analysis.

"""

 
# 4️⃣ Initialize LLM
from langchain_openai import ChatOpenAI
import os
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL"),  # default to gpt-4o
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.8
    )

  
from langchain_core.prompts import PromptTemplate


# 3️⃣ Prompts
# Step 1: Campaign idea
campaign_prompt = PromptTemplate.from_template(
    "Generate an innovative marketing campaign idea for the product: {product}."
)

# Step 2: Tagline
tagline_prompt = PromptTemplate.from_template(
    "Based on this campaign idea, suggest a catchy tagline:\n{campaign_idea}"
)

# Step 3: Risk analysis
risk_prompt = PromptTemplate.from_template(
    "Analyze potential risks or challenges for this campaign and suggest mitigation strategies:\n{campaign_with_tagline}"
)

print("=== Marketing Campaign Advisor ===")
print("Type 'exit' to quit\n")

while True:
    product = input("Enter product name or description: ").strip()
    if product.lower() == "exit":
        break

    # Step 1: Campaign idea
    campaign_response = llm.invoke(campaign_prompt.invoke({"product": product}))

    # Step 2: Tagline
    tagline_response = llm.invoke(tagline_prompt.invoke({"campaign_idea": campaign_response.content}))

    # Step 3: Risk analysis
    risk_response = llm.invoke(risk_prompt.invoke({"campaign_with_tagline": tagline_response.content}))

    # Output results
    print("\n--- Campaign Idea ---")
    print(campaign_response.content)
    print("\n--- Suggested Tagline ---")
    print(tagline_response.content)
    print("\n--- Risk Analysis ---")
    print(risk_response.content)
    print("-------------------------------\n")
