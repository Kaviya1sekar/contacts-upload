import time
import os

class Nodes():
    def get_file_path(self, state):
        print("# Checking for new files in the directory")
        path = "/Users/rakshit.bhasin/Desktop/contact_files"
        file_path = ""
        os.chdir(path)  
        contact_files = os.listdir()
        print(f"Contact files in directory: {contact_files}")
        for contact_file in contact_files:
          if contact_file.endswith(".DS_Store"):
            continue
          file_path = f"{path}/{contact_file}"
        print(f"Following contact file needs to be processed: {file_path}")
        return {
			**state,
			"file_path": file_path,
		}
        
    def wait_next_run(self, state):
        print("## Waiting for 30 seconds")
        time.sleep(30)
        return state
      
    def clear_files(self, state):
        path = "/Users/rakshit.bhasin/Desktop/contact_files"
        os.chdir(path)  
        contact_files = os.listdir()
        print(f"Contact files in directory: {contact_files}")
        for contact_file in contact_files:
          if contact_file.endswith(".DS_Store"):
            continue
          os.remove(f"{path}/{contact_file}")
        print(f"## Deleted all files in the directory")
        return state
    
    
    def new_files(self, state):
        if state['file_path'] == "":
            print("## No files found in the directory")
            return "end"
        else:
            print(f"## Got contact files in the directory: {state}")
            return "continue"
