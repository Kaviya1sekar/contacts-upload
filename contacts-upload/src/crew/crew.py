from crewai import Crew

from .agents import ContactsUploadAgents
from .tasks import ContactsUploadTasks

class ContactsUploadCrew():
	def __init__(self):
		agents = ContactsUploadAgents()
		self.contacts_extract_agent = agents.contacts_extract_agent()
		self.contacts_upload_agent = agents.contacts_upload_agent()

	def kickoff(self, state):
		print("### Kickoff Contacts Upload Crew ###")
		tasks = ContactsUploadTasks()
		extract_contacts_task = tasks.extract_contacts(self.contacts_extract_agent, state['file_path'])
		upload_contacts_task = tasks.upload_contacts(self.contacts_upload_agent, context=[extract_contacts_task])
		crew = Crew(
			agents=[
       			self.contacts_extract_agent,
				self.contacts_upload_agent
          	],
			tasks=[
				extract_contacts_task,
				upload_contacts_task
			],
			verbose=True
		)
		result = crew.kickoff()
		return {**state, "contacts_uploaded": result}
