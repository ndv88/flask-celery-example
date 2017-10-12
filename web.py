import celery
from flask import Flask, request, jsonify

app = Flask(__name__)

celery_app = celery.Celery()
celery_app.config_from_object('config')

add_task = celery_app.signature('worker.add')


@app.route('/')
def index():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))

    async_result = add_task.apply_async(args=(a, b))

    return jsonify(result=async_result.get())


if __name__ == '__main__':
    app.run(debug=True)
