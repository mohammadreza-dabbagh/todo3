from sqlalchemy.orm import Session
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate, TaskSchema
from app.models.task import Task

class TaskService:
    
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    def create_task(self, task_data: TaskCreate) -> Task:
        
        return self.task_repo.create(task_data)
    
    def get_all_tasks(self) -> list[Task]:
        return self.task_repo.get_all()

    