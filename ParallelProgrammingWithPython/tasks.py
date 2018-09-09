from math import sqrt
from celery import Celery

app = Celery("tasks", broker="redis://127.00.1:6379/0")

app.conf.CELERY_RESULT_BACKEND = "redis://172.0.0.1:6379/0"


@app.task
def squre_root(value):
    return sqrt(value)