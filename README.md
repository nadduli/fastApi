# Daniel's Social API
  A simple fully featured blog type API with options of performing Authentication, CRUD operations, Schema Validation and Documentation. 

## Requirements
### Applications
* FastAPI Framework
* Postgres Database
* Postman to test API endpoints.

### Virtual Environment 
* The required environment variables should be stored in a file named .env and each line should have the format Name=Value.
* The virtual environment should be activated to enable the project to run using this command > source env/bin/activate

### Installation
* Clone this repository and switch to the cloned repository's directory.
    using git clone https://github.com/nadduli/fastApi.git
* cd fastApi
* code . to open the project using Vscode

* Activate Pylance Extension on VS Code IDE
* Install the fastApi packages using yarn install or npm install.
* python3 -m venv env
* source ./env/bin/activate
* python -m pip install --upgrade pip
* pip install -r requirements.txt

### Launch the fastApi using
* uvicorn app.main:app --reload 
* visit the localhost and test the application using json format


