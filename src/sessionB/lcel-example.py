"""
LCEL example: Product Review Summarizer
"""

from langchain_openai import ChatOpenAI
 
# 1. Initialize the LLM
import os
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL"),  # default to gpt-4o
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.8
    )

# 2. Import necessary LCEL components
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
 

 
# 3. Create a prompt template with variables
prompt = ChatPromptTemplate.from_template("""
You are a product review summarizer.
Summarize the following review in 1 concise sentence.

Review: {review_text}
""")

# 4. Create the parser
parser = StrOutputParser()

# 5. Build the LCEL chain
chain = prompt | llm | parser

# 6. Example reviews
reviews = [
    "This phone's battery lasts two days, the camera is crystal clear, but it's a bit heavy.",
    "The laptop is super fast and light, but the fan is noisy when gaming.",
]

# 7. Run the chain for each review
for r in reviews:
    summary = chain.invoke(input={"review_text": r})
    print("Original:", r)
    print("Summary:", summary)
    print("---")