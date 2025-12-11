from typing import Generator
from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.session import SessionLocal, get_db 
from app.services.task import TaskService 
from app.repositories.task import TaskRepository 

def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    """تامین کننده TaskService برای تزریق در Router"""
    

    task_repo = TaskRepository(db=db)
    

    return TaskService(task_repo=task_repo)