

from app.db.session import get_db
from app.dependencies import get_task_service
from datetime import datetime
from app.models.task import Task
from typing import List, Iterator
from app.db.session import SessionLocal

def close_overdue_tasks():
  
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running Overdue Task Closer...")
    
    db_generator: Iterator[SessionLocal] = get_db()
    closed_count = 0
    
    try:
        
        db_session = next(db_generator)
        task_service = get_task_service(db_session)
        
        
        overdue_tasks: List[Task] = task_service.get_overdue_tasks()
        
        if not overdue_tasks:
            print("-> No open overdue tasks found. Exiting.")
            return

        print(f"-> Found {len(overdue_tasks)} open tasks past deadline.")
        
        
        for task in overdue_tasks:
        
            task_service.close_task(task.id) 
            closed_count += 1
            print(f"   - CLOSED Task ID {task.id}: {task.title}")
            
    except Exception as e:
        print(f"\n--- Error during command execution --- \n{e}")
    finally:
        
        try:
            next(db_generator) 
        except StopIteration:
            pass
            
    print(f"-> Successfully closed {closed_count} tasks.")
    print("----------------------------------------------------------------")

if __name__ == "__main__":
    close_overdue_tasks()