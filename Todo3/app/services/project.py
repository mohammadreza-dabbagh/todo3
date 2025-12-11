

from typing import List, Optional
from app.repositories.project import ProjectRepository
from app.models.project import Project
from app.services.base import BaseService

class ProjectService(BaseService):
   
    
    
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def create_project(self, name: str) -> Optional[Project]:
        
        
        
        if self.repository.get_by_name(name):
            print(f"Error: Project '{name}' already exists.")
            return None
        
        return self.repository.create(name=name)

    def get_all_projects(self) -> List[Project]:
        
        return self.repository.get_all()

    def delete_project(self, project_id: int) -> bool:
        
        project = self.repository.get_by_id(project_id)
        if not project:
            return False
        
        self.repository.delete(project)
        return True