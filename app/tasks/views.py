from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .task import handle_uploaded_file, long_computational_task
# Create your views here.

def file_upload_task(request):
    task_id = ""
    if request.method=='POST':
        #binding the data with a new form object.
        #request.POST is a dict like object containing all the request parameters but doesn't include files.
        print(request)
        form  = UploadFileForm(request.POST,request.FILES)
        print(request.FILES)       
        if form.is_valid():
            #perform some operation
            result = long_computational_task.delay(12)
            #result =  handle_uploaded_file.delay(request.FILES['file'])
            print(result.id)
            return HttpResponseRedirect('/success/')
    else:
        form  = UploadFileForm()
    
    #render the from 
    return render(request,'tasks/index.html',{'form':form})



def file_operation_task(request):
    task_id = ""
    return HttpResponse("your task id is %s", task_id)

def check_task_status(request):
    task_id = request.task_id
    return HttpResponse("your status is")

def pause_task(request):
    task_id = request.task_id
    return HttpResponse("your task is paused")

def resume_task(request):
    task_id = request.task_id
    return HttpResponse("your task is resumed")

def terminate_task(request):
    task_id = request.task_id
    return HttpResponse("your task is terminated")


