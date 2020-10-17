from celery import Celery

app1 = Celery('app',backend='mongodb://localhost:27017/',broker ='amqp://localhost',include=['tasks.task'])




if __name__ == '__main__':
    app1.start()