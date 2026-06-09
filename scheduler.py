from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from database import SessionLocal
from models import Task as Task_Model
from twilio_service import send_whatsapp_message

def  check_deadline():
    #Lets open up the database session
    db = SessionLocal()
    
    try:
        # Fetch all tasks that are not done
        tasks = db.query(Task_Model).filter(Task_Model.reminded=="False").all()
        
        #Getting the time for now
        now = datetime.now()
        
        #Calculating the time left for the tasks
        for task in tasks:
            time_left = task.deadline - now
            minutes_left = time_left.total_seconds()/60
            
            #Now deadline within 1 hour and is not reminded
            if 0 < minutes_left <=60 and not task.reminded:
                send_whatsapp_message(
                    task_name = task.name,
                    deadline = str(task.deadline),
                    missed = False
                )
                task.reminded = True
                db.commit()
            
            # Now deadline has passed and task is overdue
            if 0 > minutes_left and not task.overdue:
                send_whatsapp_message(
                    task_name = task.name,
                    deadline = str(task.deadline),
                    missed = True
                )
                task_overdue = True
                db.commit()
    finally:
        db.close()
        
#Now lets run the scheduler every 5 minutes

scheduler = BackgroundScheduler()

#Now lets run it every 5 minutes
scheduler.add_job(check_deadline,"interval",minutes=5)
