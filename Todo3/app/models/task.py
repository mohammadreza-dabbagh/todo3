

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
from datetime import timedelta 

class Task(Base):
    __tablename__ = "tasks" 
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True) 
    status = Column(String, default="pending") 
    deadline = Column(DateTime, nullable=False) 
    closed_at = Column(DateTime, nullable=True) 
    
    
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    
    project = relationship("Project", back_populates="tasks")
    
    def __repr__(self):
        return f"<Task(title='{self.title}', status='{self.status}')>"