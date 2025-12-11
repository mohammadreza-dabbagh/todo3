from fastapi import FastAPI
import uvicorn

from app.api.v1 import tasks

app = FastAPI(
    title="ToDoList Web API",
    version="v1",
    description="RESTful API for managing ToDo tasks, built on layered architecture."
)

app.include_router(tasks.router, prefix="/api/v1")

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "ToDoList API is running successfully!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)