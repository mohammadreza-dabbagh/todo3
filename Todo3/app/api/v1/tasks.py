from fastapi import APIRouter, status, Depends
from typing import List

from app.schemas.task import TaskCreate, TaskSchema

from app.dependencies import get_task_service 
from app.services.task import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    response_model=TaskSchema,
    status_code=status.HTTP_201_CREATED,
    summary="ایجاد یک وظیفه جدید"
)
async def create_task(
    task_in: TaskCreate, 
    
    task_service: TaskService = Depends(get_task_service) 
):
    
    new_task = task_service.create_task(task_data=task_in)
    
    return new_task


@router.get(
    "/",
    response_model=List[TaskSchema],
    summary="دریافت لیست تمام وظایف"
)
async def read_tasks(
    task_service: TaskService = Depends(get_task_service) 
):
    tasks_list = task_service.get_all_tasks()
    return tasks_list