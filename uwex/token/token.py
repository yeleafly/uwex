# coding=utf-8
import requests
import config
from uwex.common.uredis import rpool


def refresh_access_token():
    "刷新微信的access_token"
    token_para = {'grant_type': 'client_credential', 'appid': config.app_id, 'secret': config.app_secret}
    r = requests.get(config.url_wechat_access_token, token_para)
    # save token to redis
    rpool.set(config.redis_access_token_key, r.text)
    return r.text


def get_access_token():
    "从redis中取微信token"
    access_token = rpool.get(config.redis_access_token_key)
    if access_token != '':
        access_token = refresh_access_token()
