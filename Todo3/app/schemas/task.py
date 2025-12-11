from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    
    title: str = Field(..., max_length=100, description="عنوان وظیفه (حداکثر 100 کاراکتر)")
    description: Optional[str] = Field(None, description="توضیحات اختیاری وظیفه")
    due_date: Optional[datetime] = Field(None, description="تاریخ سررسید وظیفه")


class TaskCreate(TaskBase):
    
    pass

class TaskSchema(TaskBase):
    id: int = Field(..., description="شناسه‌ی منحصر به فرد وظیفه")
    is_completed: bool = Field(False, description="وضعیت انجام شدن وظیفه")
    created_at: datetime = Field(..., description="تاریخ ایجاد وظیفه")

    class Config:
        
        from_attributes = True