# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('check_token')
def check_token():
    return "ok"


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=9001)

