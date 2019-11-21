from RestClient4py.client import RestClient
from API_Wrap import util
import json
import re


kakao_native_app_key, kakao_rest_api_key, kakao_javascript_key, kakao_admin_key = util.kakao_auth()
client = RestClient()
client.set_header("Authorization", "KakaoAK {}".format(kakao_rest_api_key))
client.set_header("Accept", "*/*")

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingWeb(query, sort=None, page=None, size=None):

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be string type")
        elif sort not in ["accuracy", "recency"]:
            raise AttributeError("[ERROR] sort parameter should be one of [accuracy / recency]")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")
        elif page < 1 or 50 < page:
            raise AttributeError("[ERROR] page parameter should be between 1 ~ 50")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 50 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 50")

    getData = {
        "query": query,
        "sort": sort,
        "page": page,
        "size": size
    }

    return client.get("https://dapi.kakao.com/v2/search/web", params=getData)

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingVideo(query, sort=None, page=None, size=None):

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be string type")
        elif sort not in ["accuracy", "recency"]:
            raise AttributeError("[ERROR] sort parameter should be one of [accuracy / recency]")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")
        elif page < 1 or 15 < page:
            raise AttributeError("[ERROR] page parameter should be between 1 ~ 15")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 30 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 30")

    getData = {
        "query": query,
        "sort": sort,
        "page": page,
        "size": size
    }

    return client.get("https://dapi.kakao.com/v2/search/vclip", params=getData)

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingImage(query, sort=None, page=None, size=None):

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be string type")
        elif sort not in ["accuracy", "recency"]:
            raise AttributeError("[ERROR] sort parameter should be one of [accuracy / recency]")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")
        elif page < 1 or 50 < page:
            raise AttributeError("[ERROR] page parameter should be between 1 ~ 50")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 80 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 80")

    getData = {
        "query": query,
        "sort": sort,
        "page": page,
        "size": size
    }

    return client.get("https://dapi.kakao.com/v2/search/image", params=getData)

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingBlog(query, sort=None, page=None, size=None):

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be string type")
        elif sort not in ["accuracy", "recency"]:
            raise AttributeError("[ERROR] sort parameter should be one of [accuracy / recency]")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")
        elif page < 1 or 50 < page:
            raise AttributeError("[ERROR] page parameter should be between 1 ~ 50")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 50 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 50")

    getData = {
        "query": query,
        "sort": sort,
        "page": page,
        "size": size
    }

    return client.get("https://dapi.kakao.com/v2/search/blog", params=getData)

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingTIP():
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingBooks():
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingCafe():
    """TODO"""
