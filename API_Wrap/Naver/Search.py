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
        "d_titl": d_titl,
        "d_auth": d_auth,
        "d_cont": d_cont,
        "d_isbn": d_isbn,
        "d_publ": d_publ,
        "d_dafr": d_dafr,
        "d_dato": d_dato,
        "d_catg": d_catg,
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
    URL: https://developers.naver.com/products/search/
"""
def searchingCafe(query, display=None, start=None, sort=None):

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

    return client.get("https://openapi.naver.com/v1/search/cafearticle.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingKIN(query, display=None, start=None, sort=None):

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
        elif sort not in ["sim", "date", "point"]:
            raise AttributeError("[ERROR] sort parameter value should be [sim / date / point]")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort,
    }

    return client.get("https://openapi.naver.com/v1/search/kin.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingLocal(query, display=None, start=None, sort=None):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    if display:
        if type(display) != int:
            raise AttributeError("[ERROR] display parameter should be int")
        elif display < 1 or 30 < display:
            raise AttributeError("[ERROR] display parameter value should be in 1 ~ 30")

    if start:
        if type(start) != int:
            raise AttributeError("[ERROR] start parameter should be int")
        elif start < 1 or 1000 < start:
            raise AttributeError("[ERROR] start parameter value should be in 1 ~ 1,000")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be str")
        elif sort not in ["random", "comment"]:
            raise AttributeError("[ERROR] sort parameter value should be [random / comment]")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort,
    }

    return client.get("https://openapi.naver.com/v1/search/kin.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def correctingTypo(query):

    client.set_header("Accept", "*/*")

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string")

    getData = {
        "query": query,
    }

    return client.get("https://openapi.naver.com/v1/search/errata.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingWeb(query, display=None, start=None):

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

    return client.get("https://openapi.naver.com/v1/search/webkr.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingImage(query, display=None, start=None, sort=None, filter=None):

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

    if filter:
        if type(filter) != str:
            raise AttributeError("[ERROR] filter parameter should be str")
        elif filter not in ["all", "large", "medium", "small"]:
            raise AttributeError("[ERROR] filter parameter value should be [all / large / medium / small]")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort,
        "filter": filter,
    }

    return client.get("https://openapi.naver.com/v1/search/image", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingShopping(query, display=None, start=None, sort=None):

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
        elif sort not in ["sim", "date", "asc", "dsc"]:
            raise AttributeError("[ERROR] sort parameter value should be [sim / date / asc / dsc]")

    getData = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort,
    }

    return client.get("https://openapi.naver.com/v1/search/shop.json", params=getData)

"""
    URL: https://developers.naver.com/products/search/
"""
def searchingDocument(query, display=None, start=None):

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

    return client.get("https://openapi.naver.com/v1/search/doc.json", params=getData)