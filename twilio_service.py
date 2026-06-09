from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
account_auth = os.getenv("TWILIO_AUTH_SID")
from_number = os.getenv("TWILIO_NUMBER")
to_number = os.getenv("MY_NUMBER")

client = Client(account_sid,account_auth)

def send_whatsapp_message(task_name:str,deadline:str,missed:bool=False):
    if missed:
        msg = f"Hey idiot how could you forgot{task_name} and missed the {deadline}.Okay Now bring me Some Hotpot"
    else:
        msg = f"Hey Scherbatsky SUIT UP! and complete the {task_name} otherwise you will miss the {deadline}"
    client.messages.create(
        from_=from_number,
        to_number=to_number,
        body=msg
    )