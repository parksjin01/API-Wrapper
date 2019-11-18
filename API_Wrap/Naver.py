#-*- coding:utf-8 -*-

from RestClient4py.client import RestClient
from API_Wrap import util
import json


client_id, client_secret = util.naver_auth()
client = RestClient()
client.set_header("X-Naver-Client-Id", client_id)
client.set_header("X-Naver-Client-Secret", client_secret)
client.set_header("Accept", "*/*")

"""
    URL: https://developers.naver.com/products/datalab/
"""
def datalab_search(startDate, endDate, timeUnit, keywordGroups, device=None, gender=None, ages=None):

    if True:
        if type(startDate) != str:
            raise AttributeError("[ERROR] startDate parameter should be string with format yyyy-mm-dd")

        if type(endDate) != str:
            raise AttributeError("[ERROR] endDate parameter should be string with format yyyy-mm-dd")

        if type(timeUnit) != str:
            raise AttributeError("[ERROR] timeUnit parameter should be string")
        elif timeUnit not in ["date", "week", "month"]:
            raise AttributeError("[ERROR] timeUnit parameter should be one of [date / week / month]")

        if type(keywordGroups) != list:
            raise AttributeError("[ERROR] keywordGroups parameter should be list of dictionary {groupName: \"\", keywords: \"\"}")
        if len(keywordGroups) > 5:
            raise AttributeError("[ERROR] Maximum length of keywordGroups parameter is 5")
        else:
            for keyword in keywordGroups:
                if type(keyword) != dict:
                    raise AttributeError("[ERROR] Element of keywordGroups parameter should be dictionary")

                try:
                    if type(keyword["groupName"]) != str:
                        raise AttributeError("[ERROR] Value of key `groupName` in keywordGroups parameter should be string")
                except:
                    raise AttributeError("[ERROR] Key `groupName` is necessary in element of keywordGroups parameter")

                try:
                    if type(keyword["keywords"]) != list:
                        raise AttributeError("[ERROR] Value of key `keywords` in keywordGroups parameter should be list of string")
                    for k in keyword["keywords"]:
                        if type(k) != str:
                            raise AttributeError("[ERROR] Value in list of keywordGroups.keywords should be string")
                except:
                    raise AttributeError("[ERROR] Key `keywords` is necessary in element of keywordGroups parameter")

        if device and type(device) != str:
            raise AttributeError("[ERROR] device parameter should be string")

        if gender and type(gender) != str:
            raise AttributeError("[ERROR] gender parameter should be string")
        elif gender and gender not in ["m", "f"]:
            raise AttributeError("[ERROR] gender parameter should be one of [f / m]")

        if ages and type(ages) != list:
            raise AttributeError("[ERROR] ages parameter should be list of string")
        elif ages:
            for age in ages:
                if type(age) != str:
                    raise AttributeError("[ERROR] Element of ages parameter should be string")
                if int(age) < 1 or int(age) > 10:
                    raise AttributeError("[ERROR] Element value of ages parameter should be between 1 ~ 10")

    client.set_header("Content-Type", "application/json")

    posting_data = {
        "startDate": startDate,
        "endDate": endDate,
        "timeUnit": timeUnit,
        "keywordGroups": keywordGroups,
    }

    return client.post("https://openapi.naver.com/v1/datalab/search", data=json.dumps(posting_data).encode("utf-8"))


"""
    URL: https://developers.naver.com/products/datalab/
"""
def datalab_shopping(startDate, endDate, timeUnit, category, device=None, gender=None, ages=None):

    if True:
        if type(startDate) != str:
            raise AttributeError("[ERROR] startDate parameter should be string with format yyyy-mm-dd")

        if type(endDate) != str:
            raise AttributeError("[ERROR] endDate parameter should be string with format yyyy-mm-dd")

        if type(timeUnit) != str:
            raise AttributeError("[ERROR] timeUnit parameter should be string")
        elif timeUnit not in ["date", "week", "month"]:
            raise AttributeError("[ERROR] timeUnit parameter should be one of [date / week / month]")

        if type(category) != list:
            raise AttributeError("[ERROR] category parameter should be list of dictionary {groupName: \"\", keywords: \"\"}")
        if len(category) > 3:
            raise AttributeError("[ERROR] Maximum length of category parameter is 3")
        else:
            for keyword in category:
                if type(keyword) != dict:
                    raise AttributeError("[ERROR] Element of category parameter should be dictionary")

                try:
                    if type(keyword["name"]) != str:
                        raise AttributeError("[ERROR] Value of key `name` in category parameter should be string")
                except:
                    raise AttributeError("[ERROR] Key `name` is necessary in element of category parameter")

                try:
                    if type(keyword["param"]) != list:
                        raise AttributeError("[ERROR] Value of key `param` in category parameter should be list of string")
                    for k in keyword["param"]:
                        if type(k) != str:
                            raise AttributeError("[ERROR] Value in list of category.param should be string")
                except:
                    raise AttributeError("[ERROR] Key `param` is necessary in element of category parameter")

        if device and type(device) != str:
            raise AttributeError("[ERROR] device parameter should be string")

        if gender and type(gender) != str:
            raise AttributeError("[ERROR] gender parameter should be string")
        elif gender and gender not in ["m", "f"]:
            raise AttributeError("[ERROR] gender parameter should be one of [f / m]")

        if ages and type(ages) != list:
            raise AttributeError("[ERROR] ages parameter should be list of string")
        elif ages:
            for age in ages:
                if type(age) != str:
                    raise AttributeError("[ERROR] Element of ages parameter should be string")
                if int(age) < 1 or int(age) > 10:
                    raise AttributeError("[ERROR] Element value of ages parameter should be between 1 ~ 10")

    client.set_header("Content-Type", "application/json")

    posting_data = {
        "startDate": startDate,
        "endDate": endDate,
        "timeUnit": timeUnit,
        "category": category,
    }

    return client.post("https://openapi.naver.com/v1/datalab/shopping/categories", data=json.dumps(posting_data).encode("utf-8"))


"""
    URL: https://developers.naver.com/products/search/
"""
def searching():
    """TODO"""

"""
    URL: https://developers.naver.com/products/shortenurl/
"""
def shortenURL(url):

    if True:
        if type(url) != str:
            raise AttributeError("[ERROR] url parameter should be string")

    client.set_header("Content-Type", "application/x-www-form-urlencoded")
    return client.post("https://openapi.naver.com/v1/util/shorturl.json", data={"url": url})

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