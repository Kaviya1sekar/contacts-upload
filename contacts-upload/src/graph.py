from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph

from .state import ContactsState
from .nodes import Nodes
from .crew.crew import ContactsUploadCrew

class WorkFlow():
	def __init__(self):
		print("### Initializing Contacts Upload Workflow ###")
		nodes = Nodes()
		workflow = StateGraph(ContactsState)

		workflow.add_node("get_file_path", nodes.get_file_path)
		workflow.add_node("wait_next_run", nodes.wait_next_run)
		workflow.add_node("upload_contacts_to_db", ContactsUploadCrew().kickoff)
		workflow.add_node("clear_files", nodes.clear_files)

		workflow.set_entry_point("get_file_path")
		workflow.add_conditional_edges(
				"get_file_path",
				nodes.new_files,
				{
					"continue": 'upload_contacts_to_db',
					"end": 'wait_next_run'
				}
		)
		workflow.add_edge('upload_contacts_to_db', 'clear_files')
		workflow.add_edge('clear_files', 'wait_next_run')
		workflow.add_edge('wait_next_run', 'get_file_path')
		self.app = workflow.compile()