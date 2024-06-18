from crewai import Task
from textwrap import dedent
from .tools import ContactsUploadTools


class ContactsUploadTasks:
	def extract_contacts(self, agent, file_path):
		return Task(
			description=dedent(f"""\
				For the file path provided, use the provided "File Read Tool" to read the contents of the file.

				File Path
				-------
				{file_path}

				After reading the contents of the file, extract the following information from the file and 
    			provide it in a single JSON object with the following structure: 
				- file_name: name of the file
				- Contact 1
					- contact_name: full name of the contact
					- email: email address of the contact
					- phone_number: phone number of the contact with country code
					- company_name: name of the company the contact belongs to
					- department: department of the contact in the company
					- address: complete address of the contact
				- Contact 2
					(same as above)
				- ...
    
				You must extract the specified fields accurately, using relevant synonyms if necessary, without including any extraneous information.
    			Ensure the extraction is comprehensive and focuses solely on the required fields.
				Your final answer MUST be a single JSON containing all the contacts extracted from the file in the above format.
    
				NOTE: 
    			- Do not map unrelated fields, such as "relationship" (e.g., client, friend), to "department".
				- Ensure there are no special characters or unnecessary spaces in the extracted data.
				"""),
			agent=agent,
			tools=[ContactsUploadTools.file_read_tool]
		)  
  
	def upload_contacts(self, agent, context):
		return Task(
			description=dedent(f"""\
				Carefully read the JSON provided by the "extract_contacts" task, understand it completely 
    			and create an SQL query to batch insert the data into the "automation.contacts" table.
				The batch insert query must contain the following columns (use the exact names):
				- file_name (string)
				- contact_name (string)
				- email (string)
				- phone_number (string)
				- company_name (string)
				- department (string)
				- address (string)
    
				You MUST create a single SQL query to insert all the data provided in the JSON.
				Use the provided "SQL Query Executor" tool to execute the SQL query.
				Your final answer MUST be the result of the SQL query execution.
				"""),
			agent=agent,
			tools=[ContactsUploadTools.query_executor],
			context=context
		)


  
