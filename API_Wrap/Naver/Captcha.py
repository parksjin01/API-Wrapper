#-*- coding:utf-8 -*-

from RestClient4py.client import RestClient
from API_Wrap import util
import json
import re


client_id, client_secret = util.naver_auth()
client = RestClient()
client.set_header("X-Naver-Client-Id", client_id)
client.set_header("X-Naver-Client-Secret", client_secret)
client.set_header("Accept", "*/*")

def imageCaptchaVerification(key, value):
    client.set_header("Accept", "*/*")
    result = client.get("https://openapi.naver.com/v1/captcha/nkey", params={"code": 1, "key": key, "value": value})
    return result

def voiceCaptchaVerification(key, value):
    client.set_header("Accept", "*/*")
    result = client.get("https://openapi.naver.com/v1/captcha/skey", params={"code": 1, "key": key, "value": value})
    return result

"""
    URL: https://developers.naver.com/products/captcha/
"""
def imageCaptcha():
    client.set_header("Accept", "*/*")
    code = json.loads(client.get("https://openapi.naver.com/v1/captcha/nkey?code=0"))["key"]
    image = client.get("https://openapi.naver.com/v1/captcha/ncaptcha.bin", params={"key": code})
    return code, image

"""
    URL: https://developers.naver.com/produects/captach
"""
def voiceCaptcha():
    client.set_header("Accept", "*/*")
    code = json.loads(client.get("https://openapi.naver.com/v1/captcha/skey?code=0"))["key"]
    voice = client.get("https://openapi.naver.com/v1/captcha/scaptcha", params={"key": code})
    return code, voice