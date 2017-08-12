# coding=utf-8
from flask import Flask, request
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/check_token')
def check_token():
    return request.args.get('echostr')




if __name__ == '__main__':
    app.debug = True
    handler = RotatingFileHandler('uwex.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='127.0.0.1', port=9001)





