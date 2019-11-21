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
def searchingTIP(query, sort=None, page=None, size=None):

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

    return client.get("https://dapi.kakao.com/v2/search/tip", params=getData)

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingBooks(query, sort=None, page=None, size=None, target=None):

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be string type")
        elif sort not in ["accuracy", "latest"]:
            raise AttributeError("[ERROR] sort parameter should be one of [accuracy / latest]")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")
        elif page < 1 or 100 < page:
            raise AttributeError("[ERROR] page parameter should be between 1 ~ 100")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 50 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 50")

    if target:
        if type(target) != str:
            raise AttributeError("[ERROR] target parameter should be string type")
        elif target not in ["title", "isbn", "publisher", "person"]:
            raise AttributeError("[ERROR] target parameter should be one of [title / isbn / publisher / person]")

    getData = {
        "query": query,
        "sort": sort,
        "page": page,
        "size": size,
        "targer": target,
    }

    return client.get("https://dapi.kakao.com/v3/search/book", params=getData)

"""
    https://developers.kakao.com/docs/restapi/search
"""
def searchingCafe(query, sort=None, page=None, size=None):

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

    return client.get("https://dapi.kakao.com/v2/search/cafe", params=getData)

"""
    https://developers.kakao.com/docs/restapi/local
"""
def searchingAddress(query, page=None, size=None):

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 30 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 30")

    getData = {
        "query": query,
        "page": page,
        "size": size,
    }

    return client.get("https://dapi.kakao.com/v2/local/search/address.json", params=getData)
"""
    https://developers.kakao.com/docs/restapi/local
"""
def coord2regionCode(longitude, latitude, input_coord=None, output_coord=None, lang=None):

    if type(longitude) != str:
        raise AttributeError("[ERROR] longitude attribute should be string type")

    if type(latitude) != str:
        raise AttributeError("[ERROR] latitude attribute should be string type")

    if input_coord:
        if type(input_coord) != str:
            raise AttributeError("[ERROR] input_coord attribute should be string type")
        elif input_coord not in ["WGS84", "WCONGNAMUL", "CONGNAMUL", "WTM", "TM"]:
            raise AttributeError("[ERROR] input_coord attribute should be one of [WGS / WCONGNAMUL / CONGNAMUL / WTM / TM]")

    if output_coord:
        if type(output_coord) != str:
            raise AttributeError("[ERROR] output_coord attribute should be string type")
        elif output_coord not in ["WGS84", "WCONGNAMUL", "CONGNAMUL", "WTM", "TM"]:
            raise AttributeError("[ERROR] output_coord attribute should be one of [WGS / WCONGNAMUL / CONGNAMUL / WTM / TM]")

    if lang:
        if type(lang) != str:
            raise AttributeError("[ERROR] lang attribute should be string type")
        elif lang not in ["ko", "en"]:
            raise AttributeError("[ERROR] lang attribute should be one of [ko / en]")

    getData = {
        "x": longitude,
        "y": latitude,
        "input_coord": input_coord,
        "output_coord": output_coord,
        "lang": lang
    }

    return client.get("https://dapi.kakao.com/v2/local/geo/coord2regioncode.json", params=getData)

"""
    https://developers.kakao.com/docs/restapi/local
"""
def coord2address(longitude, latitude, input_coord=None):

    if type(longitude) != str:
        raise AttributeError("[ERROR] longitude attribute should be string type")

    if type(latitude) != str:
        raise AttributeError("[ERROR] latitude attribute should be string type")

    if input_coord:
        if type(input_coord) != str:
            raise AttributeError("[ERROR] input_coord attribute should be string type")
        elif input_coord not in ["WGS84", "WCONGNAMUL", "CONGNAMUL", "WTM", "TM"]:
            raise AttributeError("[ERROR] input_coord attribute should be one of [WGS / WCONGNAMUL / CONGNAMUL / WTM / TM]")

    getData = {
        "x": longitude,
        "y": latitude,
        "input_coord": input_coord,
    }

    return client.get("https://dapi.kakao.com/v2/local/geo/coord2address.json", params=getData)

"""
    https://developers.kakao.com/docs/restapi/local
"""
def transcoord(longitude, latitude, input_coord=None, output_coord=None):

    if type(longitude) != str:
        raise AttributeError("[ERROR] longitude attribute should be string type")

    if type(latitude) != str:
        raise AttributeError("[ERROR] latitude attribute should be string type")

    if input_coord:
        if type(input_coord) != str:
            raise AttributeError("[ERROR] input_coord attribute should be string type")
        elif input_coord not in ["WGS84", "WCONGNAMUL", "CONGNAMUL", "WTM", "TM"]:
            raise AttributeError("[ERROR] input_coord attribute should be one of [WGS / WCONGNAMUL / CONGNAMUL / WTM / TM]")

    if output_coord:
        if type(output_coord) != str:
            raise AttributeError("[ERROR] output_coord attribute should be string type")
        elif output_coord not in ["WGS84", "WCONGNAMUL", "CONGNAMUL", "WTM", "TM"]:
            raise AttributeError("[ERROR] output_coord attribute should be one of [WGS / WCONGNAMUL / CONGNAMUL / WTM / TM]")

    getData = {
        "x": longitude,
        "y": latitude,
        "input_coord": input_coord,
        "output_coord": output_coord,
    }

    return client.get("https://dapi.kakao.com/v2/local/geo/transcoord.json", params=getData)

"""
    https://developers.kakao.com/docs/restapi/local
"""
def searchingLocalWithKeyword():
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/local
"""
def searchingLocalWithCategory():
    """TODO"""