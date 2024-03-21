from fastapi import FastAPI, BackgroundTasks
from time import sleep

app = FastAPI()

def process_notification(email,  message: str):
    sleep(7)
    print(f"sending email to {email}, message: {message}")

@app.post("/send-notifications/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    message = "hello how are you.....?"
    # process_notification(email, message)
    background_tasks.add_task(process_notification, email, message)
    return {"message": "Notification sent to the background task."}