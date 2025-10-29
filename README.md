Session A
Foundations of LLMs and Python Environments

- Intoduction to LLMs
- Setting up Virtual Environments (venvs)
- Managing dependencies with pip and requirements.txt
- Connecting to Azure OpenAI using the LangChain client


Steps to create the virtual environment with pip

Select the folder of your project
Open a terminal using Command Prompt

1.
python -m venv .venv

2.

.\.venv\Scripts\activate.bat

pip install requests

pip freeze > requirements.txt

3.
Select Python interpreter (using Ctrl-Shift-P)



4.
pip install langchain_openai langchain dotenv langchain_core
pip install -m requirements.txt

5. 
creation of .env file

####################################################

Session B
Building with LangChain and Azure OpenAI


- Introduction to LangChain Expression Language (LCEL) 
- Building a simple chain with Prompts and Models