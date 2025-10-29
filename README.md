Session A
Foundations of LLMs and Python Environments

- Intoduction to LLMs
- Setting up Virtual Environments (venvs)
- Managing dependencies with pip and requirements.txt
- Connecting to Azure OpenAI using the LangChain client


Steps to create the virtual environment with pip

Select the folder of your project
Open a terminal using Command Prompt

python -m venv .venv
.\.venv\Scripts\activate.bat
pip install requests
pip freeze > requirements.txt

Select Python interpreter (using Ctrl-Shift-P)




pip install langchain_openai langchain dotenv langchain_core

####################################################

Session B
Building with LangChain and Azure OpenAI


- Introduction to LangChain Expression Language (LCEL) 
- Building a simple chain with Prompts and Models