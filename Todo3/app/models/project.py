

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects" 

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, unique=True, index=True, nullable=False)
    
    
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Project(name='{self.name}')>"