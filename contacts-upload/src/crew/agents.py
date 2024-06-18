from textwrap import dedent
from crewai import Agent
from langchain_openai import AzureChatOpenAI, ChatOpenAI
import os
from .tools import ContactsUploadTools
os.environ["OPENAI_API_KEY"] = "NA"

class ContactsUploadAgents():
	def __init__(self):
		self.llm = AzureChatOpenAI(
		openai_api_version=os.environ.get("AZURE_OPENAI_VERSION"),
		azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
		azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
		api_key=os.environ.get("AZURE_OPENAI_KEY"),
		model="gpt-4"
		# model="Phi-3-small-128k-instruct"
	)
		# self.llm = ChatOpenAI(
    	# model = "crewai-phi3-medium",
    	# base_url = "http://localhost:11434/v1")
  
	def contacts_extract_agent(self):
		return Agent(
			role='Data Extraction Specialist',
			goal='Extract the data from the file provided to you and provide a JSON with the extracted data.',
			backstory=dedent("""\
				As a Data Extraction Specialist, you are responsible for extracting the data from the file provided to you.
				You are very good at understanding the fields that need to be extracted and carefully extract the data with 0 percent error rate.
				You are also very good at providing the extracted data in a JSON format.
			"""),
			verbose=True,
			allow_delegation=False,
			llm=self.llm,
			tools=[ContactsUploadTools().file_read_tool]
		)
  
	def contacts_upload_agent(self):
		return Agent(
			role='Data Upload Specialist',
			goal='Read the data passed to you and write the necessary SQL queries to enter the data in the database.',
			backstory=dedent("""\
				As a Data Upload Specialist, you must precisely enter ALL the data given into the SQL database, and take special care that NO data is left out.
				You are very careful in your ability to do this task with perfect precision and your 0 percent error rate.
			"""),
			verbose=True,
			allow_delegation=False,
			llm=self.llm
		)
