from django.urls import path

from .import views

urlpatterns = [
    #'tasks/upload_file'
    path('upload_file',views.file_upload_task, name = 'upload_file'),
]