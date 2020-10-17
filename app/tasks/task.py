# Create your tasks here
from __future__ import absolute_import, unicode_literals
from app.celery import app1
import time




@app1.task
def add(x, y):
    return x + y

#following is an exampe for long conputational task

@app1.task(bind=True)
def long_computational_task(self,j):
    for i in range(10000000000):
        if not self.request.called_directly:
            self.update_state(state='PROGRESS',meta={'current': i, 'total': 10000000000})

@app1.task(bind=True)
def handle_uploaded_file(self,file):
    print("task created")
    #open a destination file
    with open('tasks/uploaded_files/'+file.name,'w+') as destination:
        i =0
        total = file.size/1000
        print(total)
        for file_chunk in file.chunks(chunk_size=10):
            time.sleep(3)
            destination.write(file_chunk) 
            self.update_state(state='PROGRESS',meta={'current': i, 'total': total})
            i = i+1