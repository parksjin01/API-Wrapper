from RestClient4py.client import RestClient
from API_Wrap import util
import os
import json


kakao_native_app_key, kakao_rest_api_key, kakao_javascript_key, kakao_admin_key = util.kakao_auth()
client = RestClient()
client.set_header("Authorization", "KakaoAK {}".format(kakao_rest_api_key))
client.set_header("Accept", "*/*")

"""
    https://developers.kakao.com/docs/restapi/speech
"""
def audioRecognize(file, service_mode="DICTATION"):

    client.set_header("Content-Type", "application/octet-stream")
    service_mode = service_mode.upper()

    if type(file) != str:
        raise AttributeError("[ERROR] file parameter should be string type")
    elif not os.path.exists(file):
        raise AttributeError("[ERROR] {} file doesn't exist".format(file))
    elif not os.access(file, os.R_OK):
        raise AttributeError("[ERROR] Reading {} file permission denied".format(file))

    if type(service_mode) != str:
        raise AttributeError("[ERROR] service_mode parameter should be string type")
    elif service_mode not in ["DICTATION", "LOCAL"]:
        raise AttributeError("[ERROR] service_mode parameter should be one of [Dictation / Local]")

    with open(file, "rb") as f:
        soundData = f.read()

    client.set_header("X-DSS-Service", service_mode)
    client.set_header("Content-Length", len(soundData))

    return client.post("https://kakaoi-newtone-openapi.kakao.com/v1/recognize", data=soundData)

"""
    https://developers.kakao.com/docs/restapi/speech
    SSML GUIDE: https://developers.kakao.com/assets/guide/kakao_ssml_guide.pdf
"""
def audioSynthesize(data):

    client.set_header("Content-Type", "application/xml")

    if type(data) != str:
        raise AttributeError("[ERROR] data attribute should be string type")
    else:
        """TODO"""

    return client.post("https://kakaoi-newtone-openapi.kakao.com/v1/synthesize", data=data.encode("utf-8"))