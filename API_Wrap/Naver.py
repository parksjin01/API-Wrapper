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
def searchingBlog(query, display=None, start=None, sort=None):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    if display:
        if type(display) != int:
            raise AttributeError("[ERROR] display parameter should be int")
        elif display < 1 or 100 < display:
            raise AttributeError("[ERROR] display parameter value should be in 1 ~ 100")

    if start:
        if type(start) != int:
            raise AttributeError("[ERROR] start parameter should be int")
        elif start < 1 or 1000 < start:
            raise AttributeError("[ERROR] start parameter value should be in 1 ~ 1,000")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be str")
        elif sort not in ["sim", "date"]:
            raise AttributeError("[ERROR] sort parameter value should be [sim / date]")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort,
    }

    return client.get("https://openapi.naver.com/v1/search/blog.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingNews(query, display=None, start=None, sort=None):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    if display:
        if type(display) != int:
            raise AttributeError("[ERROR] display parameter should be int")
        elif display < 1 or 100 < display:
            raise AttributeError("[ERROR] display parameter value should be in 1 ~ 100")

    if start:
        if type(start) != int:
            raise AttributeError("[ERROR] start parameter should be int")
        elif start < 1 or 1000 < start:
            raise AttributeError("[ERROR] start parameter value should be in 1 ~ 1,000")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be str")
        elif sort not in ["sim", "date"]:
            raise AttributeError("[ERROR] sort parameter value should be [sim / date]")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort,
    }

    return client.get("https://openapi.naver.com/v1/search/news.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingBooks(query, display=None, start=None, sort=None, d_titl=None, d_auth=None, d_cont=None, d_isbn=None, d_publ=None, d_dafr=None, d_dato=None, d_catg=None):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    if display:
        if type(display) != int:
            raise AttributeError("[ERROR] display parameter should be int")
        elif display < 1 or 100 < display:
            raise AttributeError("[ERROR] display parameter value should be in 1 ~ 100")

    if start:
        if type(start) != int:
            raise AttributeError("[ERROR] start parameter should be int")
        elif start < 1 or 1000 < start:
            raise AttributeError("[ERROR] start parameter value should be in 1 ~ 1,000")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be str")
        elif sort not in ["sim", "date"]:
            raise AttributeError("[ERROR] sort parameter value should be [sim / date]")

    if d_titl:
        if type(d_titl) != str:
            raise AttributeError("[ERROR] d_titl parameter should be str")

    if d_auth:
        if type(d_auth) != str:
            raise AttributeError("[ERROR] d_auth parameter should be str")

    if d_cont:
        if type(d_cont) != str:
            raise AttributeError("[ERROR] d_cont parameter should be str")

    if d_isbn:
        if type(d_isbn) != str:
            raise AttributeError("[ERROR] d_isbn parameter should be str")

    if d_publ:
        if type(d_publ) != str:
            raise AttributeError("[ERROR] d_publ parameter should be str")

    if d_dafr:
        if type(d_dafr) != str:
            raise AttributeError("[ERROR] d_dafr parameter should be str")
        if len(d_dafr) != 8 or re.match(r"[0-9]{8}", d_dafr) != None:
            raise AttributeError("[ERROR] d_dafr parameter format should be YYYYMMDD")

    if d_dato:
        if type(d_dato) != str:
            raise AttributeError("[ERROR] d_dato parameter should be str")
        if len(d_dato) != 8 or re.match(r"[0-9]{8}", d_dato) != None:
            raise AttributeError("[ERROR] d_dato parameter format should be YYYYMMDD")

    if d_catg:
        if type(d_catg) != str:
            raise AttributeError("[ERROR] d_catg parameter should be str")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort,
    }

    return client.get("https://openapi.naver.com/v1/search/book.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def checkingAdult(query):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    getData = {
        "query": query,
    }

    return client.get("https://openapi.naver.com/v1/search/adult.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingEncyclopedia(query, display=None, start=None):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    if display:
        if type(display) != int:
            raise AttributeError("[ERROR] display parameter should be int")
        elif display < 1 or 100 < display:
            raise AttributeError("[ERROR] display parameter value should be in 1 ~ 100")

    if start:
        if type(start) != int:
            raise AttributeError("[ERROR] start parameter should be int")
        elif start < 1 or 1000 < start:
            raise AttributeError("[ERROR] start parameter value should be in 1 ~ 1,000")

    getData = {
        "query": query,
        "display": display,
        "start": start,
    }

    return client.get("https://openapi.naver.com/v1/search/encyc.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingMovie(query, display=None, start=None, genre=None, country=None, yearfrom=None, yearto=None):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    if display:
        if type(display) != int:
            raise AttributeError("[ERROR] display parameter should be int")
        elif display < 1 or 100 < display:
            raise AttributeError("[ERROR] display parameter value should be in 1 ~ 100")

    if start:
        if type(start) != int:
            raise AttributeError("[ERROR] start parameter should be int")
        elif start < 1 or 1000 < start:
            raise AttributeError("[ERROR] start parameter value should be in 1 ~ 1,000")

    if genre:
        if type(genre) != str:
            raise AttributeError("[ERROR] genre parameter should be str")
        elif genre < 1 or 28 < genre:
            raise AttributeError("[ERROR] genre parameter value should be in 1 ~ 28"
                                 "------------------------------------------------"
                                 "Genre Code | Language                  "
                                 "1          | 드라마                      "
                                 "2          | 판타지                        "
                                 "3          | 서부                      "
                                 "4          | 공포                 "
                                 "5          | 로맨스                 "
                                 "6          | 모험                     "
                                 "7          | 스릴러                  "
                                 "8          | 느와르                      "
                                 "9          | 컬트                       "
                                 "10         | 다큐멘트리                     "
                                 "11         | 코미디                     "
                                 "12         | 가족                   "
                                 "13         | 미스터리                     "
                                 "14         | 전쟁                     "
                                 "15         | 애니메이션                     "
                                 "16         | 범죄                     "
                                 "17         | 뮤지컬                     "
                                 "18         | SF                     "
                                 "19         | 액션                     "
                                 "20         | 무협                     "
                                 "21         | 에로                     "
                                 "22         | 서스펜스                     "
                                 "23         | 서사                     "
                                 "24         | 블랙코미디                     "
                                 "25         | 실험                     "
                                 "26         | 영화카툰                     "
                                 "27         | 영화음악                     "
                                 "28         | 영화패러디포스터                     ")

    if country:
        country = country.upper()
        if type(country) != str:
            raise AttributeError("[ERROR] country parameter should be str")
        elif country not in ["KR", "JP", "US", "HK", "GB", "FR", "ETC"]:
            raise AttributeError("[ERROR] genre parameter value should be in one of the below"
                                 "------------------------------------------------"
                                 "Country Code | Country Name                  "
                                 "KR           | 한국                      "
                                 "JP           | 일본                        "
                                 "US           | 미국                      "
                                 "HK           | 홍콩                 "
                                 "GB           | 영국                 "
                                 "FR           | 프랑스                     "
                                 "ETC          | 기타                  ")

    if yearfrom:
        if type(yearfrom) != str:
            raise AttributeError("[ERROR] yearfrom parameter should be str")
        if len(yearfrom) != 4 or re.match(r"[0-9]{4}", yearfrom) != None:
            raise AttributeError("[ERROR] yearfrom parameter format should be YYYY")

    if yearto:
        if type(yearto) != str:
            raise AttributeError("[ERROR] yearto parameter should be str")
        if len(yearto) != 4 or re.match(r"[0-9]{4}", yearto) != None:
            raise AttributeError("[ERROR] yearto parameter format should be YYYY")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "genre": genre,
        "country": country,
        "yearfrom": yearfrom,
        "yearto": yearto,
    }

    return client.get("https://openapi.naver.com/v1/search/movie.json", params=getData)


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