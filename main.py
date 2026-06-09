# Lets do the Fast Api thing for the tasks
from fastapi import FastAPI,HTTPException,Depends
from database import get_db,engine
from models import Task as Task_Model
from schemas import Task as Task_Schema,Update
from sqlalchemy.orm  import Session
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=" Making an Deadline Task bot using Twilio ")


#Lets add the task here
@app.post("/tasks")
def add_task(task:Task_Schema,db:Session = Depends(get_db)):
    db_task = Task_Model(
        name = task.name,
        deadline = task.deadline,
        priority = task.priority      
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#This is for showing all the tasks that are there

@app.get("/tasks")
def show_all_tasks(db:Session = Depends(get_db)):
   tasks = db.query(Task_Model).all()
   return tasks

#This is for the showing an particular task

@app.get("/tasks/{task_id}")
def show_task(task_id:int,db:Session = Depends(get_db)):
    task_one = db.query(Task_Model).filter(Task_Model.id==task_id).first()
    if not task_one:
        raise HTTPException(status_code=404,detail="The id you are searching for is not there")
    else:
        return task_one

# Now lets do the update ones

@app.put("/tasks/{task_id}")
def update_task(task:Update,task_id:int,db:Session=Depends(get_db)):
    existing_task = db.query(Task_Model).filter(Task_Model.id==task_id).first()
    if not existing_task:
        raise HTTPException(status_code=404,detail="The task you wish to change does not exist")
    
    updated_task = {k:v for k,v in task.model_dump().items()if v is not None}
    for key,value in updated_task.items():
        setattr(existing_task,key,value)
    db.commit()
    db.refresh(existing_task)
    return existing_task

    
# Lets delete the task and go to the mall

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int,db:Session = Depends(get_db)):
    task_one = db.query(Task_Model).filter(Task_Model.id==task_id).first()
    if not task_one:
        raise HTTPException(status_code=404,detail="The thing you are looking to delete is not found")
    db.delete(task_one)
    db.commit()
    return f"The task of {task_id} has been deleted"


    


    
