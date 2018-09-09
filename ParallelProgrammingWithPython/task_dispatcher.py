import logging
from celery import Celery

app = Celery("tasks", broker="redis://127.0.0.1:6397/0")
app.conf.CELERY_RESULT_BACKEND = "redis://127.0.0.1:6397/0"


def manage_sqrt_task(value):
    result = app.send_task("tasks.sqrt_task", args=(value,))
    logging.info(result.get())


if __name__ == "__main__":
    manage_sqrt_task(25)

