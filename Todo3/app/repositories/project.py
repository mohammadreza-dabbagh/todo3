from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.project import Project
from app.repositories.base import BaseRepository

class ProjectRepository(BaseRepository[Project]):
 
    def __init__(self, db: Session):
        
        super().__init__(db, Project)

    def get_by_name(self, name: str) -> Optional[Project]:
        
        return self.db.query(Project).filter(Project.name == name).first()
    
    def get_projects_with_tasks(self) -> List[Project]:
    
        return self.get_all()