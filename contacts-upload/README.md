
## Model used
This example uses GPT-4 hosted in Fourkites Azure Environment. 
## To setup and run 
- **Configure Environment**: Copy ``.env.example` and set up the environment variable.Note : To run on your machine - Fill the details of .env_example and change the filename to .env and run
- **Setup a credentials.json**: Follow the [google instructions](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application), once you’ve downloaded the file, name it `credentials.json` and add to the root of the project. This is to give the code access to the email we want to listen to. 
- **Install Dependencies**: Run `pip install -r requirements.txt`
- **Execute the Script**: Run `python main.py`
## Notes
Uses CrewAI with LangChain and LangGraph to automate the process of automatically checking emails and creating drafts and then sending response. 


