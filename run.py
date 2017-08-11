# coding=utf-8
from flask import Flask, request
import logging
from logging.handlers import RotatingFileHandler
from uwex.token import token
import time
import config

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/check_token')
def check_token():
    return request.args.get('echostr')


def timer(n):
    while True:
        print('begin to refresh access token')

        access_token = token.refresh_access_token()
        app.logger.info('access token is :{}' + access_token)
        print('access token is:{}' + access_token)
        time.sleep(n)


if __name__ == '__main__':
    app.debug = True
    handler = RotatingFileHandler('uwex.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='127.0.0.1', port=9001)
    timer(config.timer_refresh_access_token)





