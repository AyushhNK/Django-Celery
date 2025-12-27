import time
from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@app.task
def add(x, y):
    time.sleep(4)   # ✅ simulate long-running work
    return x + y

@app.task
def multiply(x, y):
    time.sleep(2)   # ✅ simulate long-running work
    return x * y


if __name__ == '__main__':
    
    print('Multiply result:', multiply.apply_async((4, 5)).get())
    print('Add result:', add.apply_async((4, 4)).get())

