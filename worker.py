import celery


app = celery.Celery()
app.config_from_object('config')


@app.task()
def add(a, b):
    return a + b
