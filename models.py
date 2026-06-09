#Now lets make the model for the thing
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from database import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    created = Column(DateTime,default=datetime.now)
    deadline = Column(DateTime,nullable=False)
    priority = Column(String,nullable=False)
    is_done = Column(Boolean,default=False)
    reminded = Column(Boolean,default=False)
    overdue = Column(Boolean,default=False)