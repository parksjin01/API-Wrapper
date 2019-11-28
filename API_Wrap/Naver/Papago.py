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
    URL: https://developers.naver.com/docs/papago/papago-nmt-overview.md
"""
def papagoNMT(sourceLang, targetLang, sentence):
    client.set_header("Accept", "*/*")
    lang = ["ko", "en", "ja", "zh-CN", "zh-TW", "vi", "id", "th", "de", "ru", "es", "it", "fr"]

    if sourceLang not in lang or targetLang not in lang:
        raise AttributeError("[ERROR] Language suppots only below 13 languages"
                             "------------------------------------------------"
                             "Num | Langauge Code | Language                  "
                             "1   | ko            | 한국어                      "
                             "2   | en            | 영어                        "
                             "3   | ja            | 일본어                      "
                             "4   | zh-CN         | 중국어 간체자                 "
                             "5   | zh-TW         | 중국어 번체자                 "
                             "6   | vi            | 베트남어                     "
                             "7   | id            | 인도네시아어                  "
                             "8   | th            | 태국어                      "
                             "9   | de            | 독일어                       "
                             "10  | ru            | 러시아어                     "
                             "11  | es            | 스페인어                     "
                             "12  | it            | 이탈리아어                   "
                             "13  | fr            | 프랑스어                     ")

    postData = {"source": sourceLang, "target": targetLang, "text": sentence}
    return client.post("https://openapi.naver.com/v1/papago/n2mt", data=postData)

"""
    URL: https://developers.naver.com/docs/papago/papago-smt-overview.md
"""
def papagoSMT(sourceLang, targetLang, sentence):
    client.set_header("Accept", "*/*")
    lang = ["ko", "en", "ja", "zh-CN", "zh-TW"]

    if sourceLang not in lang or targetLang not in lang:
        raise AttributeError("[ERROR] Language suppots only below 5 languages"
                             "------------------------------------------------"
                             "Num | Langauge Code | Language                  "
                             "1   | ko            | 한국어                      "
                             "2   | en            | 영어                        "
                             "3   | ja            | 일본어                      "
                             "4   | zh-CN         | 중국어 간체자                 "
                             "5   | zh-TW         | 중국어 번체자                 ")

    postData = {"source": sourceLang, "target": targetLang, "text": sentence}
    return client.post("https://openapi.naver.com/v1/language/translate", data=postData)

"""
    URL: https://developers.naver.com/docs/papago/papago-detectlangs-api-reference.md
"""
def detectLang(text):
    client.set_header("Accept", "*/*")

    postData = {"query": text}
    return client.post("https://openapi.naver.com/v1/papago/detectLangs", data=postData)

"""
    URL: https://developers.naver.com/docs/papago/papago-romanization-overview.md
"""
def romanization(namedEntity):
    client.set_header("Accept", "*/*")

    postData = {"query": namedEntity}
    return client.get("https://openapi.naver.com/v1/krdict/romanization", params=postData)