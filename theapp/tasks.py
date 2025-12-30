from celery import shared_task
from time import sleep

@shared_task
def sub(x, y):
    sleep(5)
    return x - y
@shared_task
def add(x, y):
    sleep(5)
    return x + y

@shared_task
def mul(x, y):
    sleep(5)
    return x * y

@shared_task
def hello_world():
    print("Hello, World!")
    return "Hello, World!"