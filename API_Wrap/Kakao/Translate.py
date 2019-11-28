from RestClient4py.client import RestClient
from API_Wrap import util
import os
import json


kakao_native_app_key, kakao_rest_api_key, kakao_javascript_key, kakao_admin_key = util.kakao_auth()
client = RestClient()
client.set_header("Authorization", "KakaoAK {}".format(kakao_rest_api_key))
client.set_header("Accept", "*/*")

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