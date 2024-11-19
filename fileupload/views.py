from django.shortcuts import render
from .tasks import process_file  
from django.http import JsonResponse
from .tasks import simulate_long_task
from .tasks import send_email_task
from .tasks import process_image
# Create your views here.

def trigger_task(request):
    simulate_long_task.delay() 
    return JsonResponse({"message": "Task is running in the background"})



def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_path = f"uploads/{uploaded_file.name}"  
        
        
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        
        process_file.delay(file_path)  
        
        return JsonResponse({"message": "File uploaded, and processing started in the background."})
    return render(request, 'library/fileupload.html') 



def send_email_view(request):
    
    subject = "Test Email"
    message = "This is a test email sent asynchronously using Celery."
    recipient_list = ['sp2309116@gmail.com']

    send_email_task.delay(subject, message, recipient_list)

    return render(request, 'library/email_sent.html')




def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        
        
        image_path = f'C:/Users/SAROJA S PAWAR/Desktop/images/{uploaded_image.name}' 
        
        with open(image_path, 'wb') as f:
            for chunk in uploaded_image.chunks():
                f.write(chunk)

        
        process_image.delay(image_path)  

        return JsonResponse({"message": "Image uploaded and processing started."})

    return render(request, 'library/upload_image.html')  
