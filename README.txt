For doubts on pipenv refer this -> https://realpython.com/pipenv-guide/

Installing pipenv once on the system if not already installed:
pip install pipenv

Everytime using the cmdline, run the below command to enter the virtual environment,
pipenv shell

Installing dependencies for once when cloning the project:
pipenv install --ignore-pipfile

On VSCODE use the shortcut Ctrl + Shift + P and type "Python: Select Interpreter" and select the option with "local-api"

Starting the server during development to see the changes immediately with hot reload:
pipenv run uvicorn main:app --reload

Starting the server on Raspberry Pi:
pipenv run uvicorn main:app