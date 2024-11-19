
# myapp/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

import time

@shared_task
def simulate_long_task():
    print("Task started...")
    time.sleep(5)  
    print("Task completed!")
    return "Task finished"


@shared_task
def process_file(file_path):
    """Simulate file processing."""
   
    time.sleep(10)  
    print(f"File {file_path} processed successfully!")
    return f"File {file_path} processed successfully!"

@shared_task
def send_email_task(subject, message, recipient_list):
    """
    A simple Celery task to send email asynchronously.
    """
    print(f"Sending email to: {recipient_list}") 
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    

    
from celery import shared_task
from PIL import Image
import os

@shared_task
def process_image(image_path):
    try:
        
        img = Image.open(image_path)
        img = img.resize((800, 800))

        output_path = os.path.join('processed_images', os.path.basename(image_path))

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        img.save(output_path)

        return f"Image processed and saved to {output_path}"
    except Exception as e:
        return f"Error processing image: {str(e)}"

