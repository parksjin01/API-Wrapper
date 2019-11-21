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
def searchingLocalWithKeyword(query, category_group_code=None, longitude=None, latitude=None, radius=None, rect=None,
                              page=None, size=None, sort=None):

    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")

    if category_group_code:
        category_group_code = category_group_code.upper()

        if type(category_group_code) != str:
            raise AttributeError("[ERROR] category_group_code parameter should be string type")
        elif category_group_code not in ["MT1", "CS2", "PS3", "SC4", "AC5", "PK6", "OL7", "SW8", "BK9", "CT1", "AG2",
                                         "PO3", "AT4", "AD5", "FD6", "CE7", "HP8", "PM9"]:
            raise AttributeError("[ERROR] category_group_code parameter should be one of below codes"
                                 "------------------------------------------------------------------"
                                 "Number    | Category_Group_Code    | Description"
                                 "1         | MT1                    | 대형마트"
                                 "2         | CS2                    | 편의점"
                                 "3         | PS3                    | 어린이집, 유치원"
                                 "4         | SC4                    | 학교"
                                 "5         | AC5                    | 학원"
                                 "6         | PK6                    | 주차장"
                                 "7         | OL7                    | 주유소, 충전소"
                                 "8         | SW8                    | 지하철역"
                                 "9         | BK9                    | 은행"
                                 "10        | CT1                    | 문화시설"
                                 "11        | AG2                    | 중개업소"
                                 "12        | PO3                    | 공공기관"
                                 "13        | AT4                    | 관광명소"
                                 "14        | AD5                    | 숙박"
                                 "15        | FD6                    | 음식점"
                                 "16        | CE7                    | 카페"
                                 "17        | HP8                    | 병원"
                                 "18        | PM9                    | 약국")

    if longitude:
        if type(longitude) != str:
            raise AttributeError("[ERROR] longitude parameter should be string type")
        if latitude == None or radius == None:
            raise AttributeError("[ERROR] longitude parameter should be used with latitude parameter and radius parameter")

    if latitude:
        if type(latitude) != str:
            raise AttributeError("[ERROR] latitude paramter should be string type")
        if longitude == None or radius == None:
            raise AttributeError("[ERROR] latitude parameter should be used with longitude parameter and radius parameter")

    if radius:
        if type(radius) != int:
            raise AttributeError("[ERROR] radius parameter should be int type")
        elif radius < 0 or 20000 < radius:
            raise AttributeError("[ERROR] radius parameter should be between 0 ~ 20,000")
        elif longitude == None or latitude == None:
            raise AttributeError("[ERROR] radius parameter should be used with longitude parameter and latitude parameter")

    if rect:
        if type(rect) != str:
            raise AttributeError("[ERROR] rect parameter should be string type")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")
        elif page < 1 or 45 < page:
            raise AttributeError("[ERROR] page parameter should be between 1 ~ 45")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 15 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 15")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be string type")
        elif sort not in ["distance", "accuracy"]:
            raise AttributeError("[ERROR] sort parameter should be one of [distance / accuracy]")

        if sort == "distance" and (longitude == None or latitude == None):
            raise AttributeError("[ERROR] When sort parameter is `distance`, it should be used with longitude and latitude")

    getData = {
        "query": query,
        "category_group_code": category_group_code,
        "x": longitude,
        "y": latitude,
        "radius": radius,
        "rect": rect,
        "page": page,
        "size": size,
        "sort": sort,
    }

    return client.get("https://dapi.kakao.com/v2/local/search/keyword.json", params=getData)

"""
    https://developers.kakao.com/docs/restapi/local
"""
def searchingLocalWithCategory(category_group_code, longitude=None, latitude=None, radius=None, rect=None,
                              page=None, size=None, sort=None):

    if category_group_code:
        category_group_code = category_group_code.upper()

        if type(category_group_code) != str:
            raise AttributeError("[ERROR] category_group_code parameter should be string type")
        elif category_group_code not in ["MT1", "CS2", "PS3", "SC4", "AC5", "PK6", "OL7", "SW8", "BK9", "CT1", "AG2",
                                         "PO3", "AT4", "AD5", "FD6", "CE7", "HP8", "PM9"]:
            raise AttributeError("[ERROR] category_group_code parameter should be one of below codes"
                                 "------------------------------------------------------------------"
                                 "Number    | Category_Group_Code    | Description"
                                 "1         | MT1                    | 대형마트"
                                 "2         | CS2                    | 편의점"
                                 "3         | PS3                    | 어린이집, 유치원"
                                 "4         | SC4                    | 학교"
                                 "5         | AC5                    | 학원"
                                 "6         | PK6                    | 주차장"
                                 "7         | OL7                    | 주유소, 충전소"
                                 "8         | SW8                    | 지하철역"
                                 "9         | BK9                    | 은행"
                                 "10        | CT1                    | 문화시설"
                                 "11        | AG2                    | 중개업소"
                                 "12        | PO3                    | 공공기관"
                                 "13        | AT4                    | 관광명소"
                                 "14        | AD5                    | 숙박"
                                 "15        | FD6                    | 음식점"
                                 "16        | CE7                    | 카페"
                                 "17        | HP8                    | 병원"
                                 "18        | PM9                    | 약국")

    if longitude:
        if type(longitude) != str:
            raise AttributeError("[ERROR] longitude parameter should be string type")
        if latitude == None or radius == None:
            raise AttributeError("[ERROR] longitude parameter should be used with latitude parameter and radius parameter")

    if latitude:
        if type(latitude) != str:
            raise AttributeError("[ERROR] latitude paramter should be string type")
        if longitude == None or radius == None:
            raise AttributeError("[ERROR] latitude parameter should be used with longitude parameter and radius parameter")

    if radius:
        if type(radius) != int:
            raise AttributeError("[ERROR] radius parameter should be int type")
        elif radius < 0 or 20000 < radius:
            raise AttributeError("[ERROR] radius parameter should be between 0 ~ 20,000")
        elif longitude == None or latitude == None:
            raise AttributeError("[ERROR] radius parameter should be used with longitude parameter and latitude parameter")

    if rect:
        if type(rect) != str:
            raise AttributeError("[ERROR] rect parameter should be string type")

    if page:
        if type(page) != int:
            raise AttributeError("[ERROR] page parameter should be int type")
        elif page < 1 or 45 < page:
            raise AttributeError("[ERROR] page parameter should be between 1 ~ 45")

    if size:
        if type(size) != int:
            raise AttributeError("[ERROR] size parameter should be int type")
        elif size < 1 or 15 < size:
            raise AttributeError("[ERROR] size parameter should be between 1 ~ 15")

    if sort:
        if type(sort) != str:
            raise AttributeError("[ERROR] sort parameter should be string type")
        elif sort not in ["distance", "accuracy"]:
            raise AttributeError("[ERROR] sort parameter should be one of [distance / accuracy]")

        if sort == "distance" and (longitude == None or latitude == None):
            raise AttributeError("[ERROR] When sort parameter is `distance`, it should be used with longitude and latitude")

    getData = {
        "category_group_code": category_group_code,
        "x": longitude,
        "y": latitude,
        "radius": radius,
        "rect": rect,
        "page": page,
        "size": size,
        "sort": sort,
    }

    return client.get("https://dapi.kakao.com/v2/local/search/category.json", params=getData)

"""
    https://developers.kakao.com/docs/restapi/translation
"""
def translation(query, src_lang, target_lang):
    if type(query) != str:
        raise AttributeError("[ERROR] query parameter should be string type")
    elif len(query) > 5000:
        raise AttributeError("[ERROR] Maximum length of query parameter should be same or less than 5,000 chars")

    if type(src_lang) != str:
        raise AttributeError("[ERROR] src_lang parameter should be string type")
    elif src_lang not in ["kr", "en", "jp", "cn", "vi", "id", "ar", "bn", "de", "es", "fr", "hi", "it", "ms", "nl",
                          "pt", "ru", "th", "tr"]:
        raise AttributeError("[ERROR] src_lang parameter should be one of below language codes"
                             "--------------------------------------------------------------"
                             "Number    | Language Code    | Language"
                             "1         | kr             | 한국어"
                             "2         | en             | 영어"
                             "3         | jp             | 일본어"
                             "4         | cn             | 중국어"
                             "5         | vi             | 베트남어"
                             "6         | id             | 인도네시아어"
                             "7         | ar             | 아랍어"
                             "8         | bn             | 뱅갈어"
                             "9         | de             | 독일어"
                             "10        | es             | 스페인어"
                             "11        | fr             | 프랑스어"
                             "12        | hi             | 힌디어"
                             "13        | it             | 이탈리아어"
                             "14        | ms             | 말레이시아어"
                             "15        | nl             | 네덜란드어"
                             "16        | pt             | 포르투갈어"
                             "17        | ru             | 러시아어"
                             "18        | th             | 태국어"
                             "19        | tr             | 터키어")

    if type(target_lang) != str:
        raise AttributeError("[ERROR] target_lang parameter should be string type")
    elif target_lang not in ["kr", "en", "jp", "cn", "vi", "id", "ar", "bn", "de", "es", "fr", "hi", "it", "ms", "nl",
                          "pt", "ru", "th", "tr"]:
        raise AttributeError("[ERROR] target_lang parameter should be one of below language codes"
                             "--------------------------------------------------------------"
                             "Number    | Language Code    | Language"
                             "1         | kr             | 한국어"
                             "2         | en             | 영어"
                             "3         | jp             | 일본어"
                             "4         | cn             | 중국어"
                             "5         | vi             | 베트남어"
                             "6         | id             | 인도네시아어"
                             "7         | ar             | 아랍어"
                             "8         | bn             | 뱅갈어"
                             "9         | de             | 독일어"
                             "10        | es             | 스페인어"
                             "11        | fr             | 프랑스어"
                             "12        | hi             | 힌디어"
                             "13        | it             | 이탈리아어"
                             "14        | ms             | 말레이시아어"
                             "15        | nl             | 네덜란드어"
                             "16        | pt             | 포르투갈어"
                             "17        | ru             | 러시아어"
                             "18        | th             | 태국어"
                             "19        | tr             | 터키어")

    postData = {
        "query": query,
        "src_lang": src_lang,
        "target_lang": target_lang
    }

    return client.post("https://kapi.kakao.com/v1/translation/translate", data=postData)

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def faceRecognition(file, image_url, threshold=None):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def productsRecognition(image, image_url, threshold=None):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def createThumbnail(file, image_url, width, height):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def detectThumbnail(file, image_url, width, height):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def createMultiTag(file, image_url):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def detectAdultImage(file, image_url):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def detectOCR(file):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def recognizeOCR(file):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/speech
"""
def audioRecognize(file):
    """TODO"""

"""
    https://developers.kakao.com/docs/restapi/speech
"""
def audioSynthesize(data):
    """TODO"""