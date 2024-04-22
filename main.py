from time import sleep
from celery import Celery

app = Celery(main='main', broker='amqp://guest:guest@localhost:5672/')


@app.task(name='main.add')
def add(a, b):
    sleep(5)
    return a + b
