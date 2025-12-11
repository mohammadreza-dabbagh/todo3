
from sqlalchemy.orm import Session
from typing import List
from app.models.task import Task
from app.repositories.base import BaseRepository
from datetime import datetime

class TaskRepository(BaseRepository[Task]):
   
    def __init__(self, db: Session):
        super().__init__(db, Task)

    def get_by_project(self, project_id: int) -> List[Task]:
        
        return self.db.query(Task).filter(Task.project_id == project_id).all()
    
    def get_overdue_and_open_tasks(self) -> List[Task]:
        
        
        return self.db.query(Task).filter(
            Task.deadline < datetime.now(),
            Task.status != 'done' 
        ).all()