

from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from app.db.base import Base 

T = TypeVar('T', bound=Base)

class BaseRepository(Generic[T]):

    def __init__(self, db: Session, model: T):
        
        self.db = db
        
        self.model = model

    def get_by_id(self, item_id: int) -> Optional[T]:
    
        return self.db.query(self.model).filter(self.model.id == item_id).first()

    def get_all(self) -> List[T]:
        
        return self.db.query(self.model).all()

    def create(self, **kwargs) -> T:

        db_item = self.model(**kwargs)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, db_item: T, **kwargs) -> T:
        
        for key, value in kwargs.items():
            setattr(db_item, key, value)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def delete(self, db_item: T):
    
        self.db.delete(db_item)
        self.db.commit()