# coding=utf-8
from uwex.token import token
import time
import config


def timer(n):
    while True:
        print('begin to refresh access token')

        access_token = token.refresh_access_token()
        print('access token is:{}' + access_token)
        time.sleep(n)


timer(config.timer_refresh_access_token)
