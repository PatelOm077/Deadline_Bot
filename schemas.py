from pydantic import BaseModel,Field
from typing import Optional
from datetime import date,datetime

class Task(BaseModel):
    name:str
    created:datetime = Field(default=datetime.now())
    deadline:datetime
    priority:str
    is_done:bool = False
    
class Update(BaseModel):
    name:Optional[str] = None
    deadline:Optional[datetime] = None
    priority:Optional[str] = None
    is_done:Optional[bool] = None