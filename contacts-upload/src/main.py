from src.graph import WorkFlow
from langchain_core.runnables import RunnableConfig
from fastapi import BackgroundTasks, FastAPI


app = FastAPI()


@app.get("/contacts-upload/")
async def email_workflow(limit: int, background_tasks: BackgroundTasks): 
    print("Starting the agentic workflow.")
    app = WorkFlow().app
    config = RunnableConfig(recursion_limit=limit)
    background_tasks.add_task(app.invoke,{},config)
    print("Started the langgraph workflow for Contacts Upload.")
    return {"message": "started the agentic workflow."}