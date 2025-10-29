 
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


 

# Prompt 1: Short story
story_prompt = PromptTemplate.from_template("Write a short, engaging story about {topic}.")
# Prompt 2: Plot twist (takes 'story' as input)
twist_prompt = PromptTemplate.from_template("Add an unexpected plot twist to the following story:\n{story}")
# Prompt 3: Moral (takes 'story_with_twist' as input)
moral_prompt = PromptTemplate.from_template("Conclude the story with a meaningful moral:\n{story_with_twist}")

print("=== Interactive Story Builder ===")
print("Type 'exit' to quit\n")

while True:
    topic = input("Enter a topic: ").strip()
    if topic.lower() == "exit":
        break

    # Step 1: story
    story_response = llm.invoke(story_prompt.invoke({"topic": topic}))

    # Step 2: plot twist
    twist_response = llm.invoke(twist_prompt.invoke({"story": story_response.content}))

    # Step 3: moral
    moral_response = llm.invoke(moral_prompt.invoke({"story_with_twist": twist_response.content}))

    print("\n--- Generated Story ---")
    print(moral_response.content)
    print("-----------------------\n")
