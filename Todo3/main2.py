
from app.db.session import get_db
from app.dependencies import get_project_service, get_task_service
from datetime import datetime, timedelta
from typing import Iterator

def main():
  
    print("--- ToDo List Application Start (Phase 2 Demo) ---")
    
  
    db_generator: Iterator[SessionLocal] = get_db()
    
    try:
        
        db_session = next(db_generator)
        
        
        project_service = get_project_service(db_session)
        task_service = get_task_service(db_session)
        
        
        print("\n[1] Creating Projects & Tasks...")
        
        project_name_1 = "Phase 2 Core"
        project_name_2 = "Personal ToDos"
        
        project1 = project_service.create_project(name=project_name_1)
        project2 = project_service.create_project(name=project_name_2)
        
        if project1 and project2:
            print(f"-> Created Project: {project1.name} (ID: {project1.id})")
            
            
            future_deadline = datetime.now() + timedelta(days=7)
            task1 = task_service.create_task(
                title="Review Business Logic", 
                description="Final checks on services.", 
                deadline=future_deadline, 
                project_id=project1.id
            )
            print(f"-> Created Task: {task1.title} (Status: {task1.status})")
            
        
            print("\n[2] Closing a Task...")
            closed_task = task_service.close_task(task1.id)
            if closed_task:
                print(f"-> CLOSED Task: {closed_task.title} (Status: {closed_task.status})")
                
            
            print("\n[3] Reading Overdue Tasks...")
            
            overdue_list = task_service.get_overdue_tasks()
            print(f"-> Found {len(overdue_list)} open overdue tasks.")

        
            print("\n[4] Deleting Project (Cascade Test)...")
            success = project_service.delete_project(project2.id)
            print(f"-> Project '{project_name_2}' deleted: {success}")
            
        else:
            print("Demo aborted.")
            
    except Exception as e:
        print(f"\n--- An Error Occurred --- \nError: {e}")
    finally:
        
        try:
            next(db_generator) 
        except StopIteration:
            pass 
        
    print("\n--- ToDo List Application End ---")


if __name__ == "__main__":
    main()