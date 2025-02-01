from celery import Celery

# Initialize Celery app with Redis as the broker
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

# To test the task
if __name__ == '__main__':
    result = add.apply_async((4, 4))  # Use async task call
    print('Task result:', result.get())  # Wait for the result
