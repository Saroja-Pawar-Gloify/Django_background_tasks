# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('trigger-task/', views.trigger_task, name='trigger_task'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('send-email/', views.send_email_view, name='send_email'),
     path('upload/', views.upload_image, name='upload_image'),
]
