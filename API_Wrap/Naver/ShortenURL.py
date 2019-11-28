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

"""
    URL: https://developers.naver.com/products/shortenurl/
"""
def shortenURL(url):

    if True:
        if type(url) != str:
            raise AttributeError("[ERROR] url parameter should be string")

    client.set_header("Content-Type", "application/x-www-form-urlencoded")
    return client.post("https://openapi.naver.com/v1/util/shorturl.json", data={"url": url})