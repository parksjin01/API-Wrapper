from RestClient4py.client import RestClient
from API_Wrap import util
import os
import json


kakao_native_app_key, kakao_rest_api_key, kakao_javascript_key, kakao_admin_key = util.kakao_auth()
client = RestClient()
client.set_header("Authorization", "KakaoAK {}".format(kakao_rest_api_key))
client.set_header("Accept", "*/*")

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def faceRecognition(file=None, image_url=None, threshold=None):

    postData = {}

    if file == None and image_url == None:
        raise AttributeError("[ERROR] One of file parameter or image_url parameter is mandatory")
    elif file != None and image_url != None:
        raise AttributeError("[ERROR] Only one of file parameter and image_url parameter can be used")

    if file:
        client.clear_header("Content-Type")
        if type(file) != str:
            raise AttributeError("[ERROR] file parameter should be string type")
        if not os.path.exists(file):
            raise AttributeError("[ERROR] {} file doesn't exist".format(file))
        if not os.access(file, os.R_OK):
            raise AttributeError("[ERROR] Opening {} file is permission denied".format(file))

    if image_url:
        client.clear_header("Content-Type")
        client.set_header("Content-Type", "application/x-www-form-urlencoded")
        if type(image_url) != str:
            raise AttributeError("[ERROR] image_url parameter should be string type")

    if threshold:
        try:
            threshold = float(threshold)
        except:
            pass

        if type(threshold) != float:
            raise AttributeError("[ERROR] threshold parameter should be float type")
        elif threshold < 0 or 1 < threshold:
            raise AttributeError("[ERROR] threshold parameter should be between 0.0 ~ 1.0")

        postData["threshold"] = threshold

    if file:
        client.files = {"file": open(file, "rb")}
    else:
        client.files = None
        postData["image_url"] = image_url

    return client.post("https://kapi.kakao.com/v1/vision/face/detect", data=postData)

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def productsRecognition(file=None, image_url=None, threshold=None):

    postData = {}

    if file == None and image_url == None:
        raise AttributeError("[ERROR] One of file parameter or image_url parameter is mandatory")
    elif file != None and image_url != None:
        raise AttributeError("[ERROR] Only one of file parameter and image_url parameter can be used")

    if file:
        client.clear_header("Content-Type")
        if type(file) != str:
            raise AttributeError("[ERROR] file parameter should be string type")
        if not os.path.exists(file):
            raise AttributeError("[ERROR] {} file doesn't exist".format(file))
        if not os.access(file, os.R_OK):
            raise AttributeError("[ERROR] Opening {} file is permission denied".format(file))

    if image_url:
        client.clear_header("Content-Type")
        client.set_header("Content-Type", "application/x-www-form-urlencoded")
        if type(image_url) != str:
            raise AttributeError("[ERROR] image_url parameter should be string type")

    if threshold:
        try:
            threshold = float(threshold)
        except:
            pass

        if type(threshold) != float:
            raise AttributeError("[ERROR] threshold parameter should be float type")
        elif threshold < 0 or 1 < threshold:
            raise AttributeError("[ERROR] threshold parameter should be between 0.0 ~ 1.0")

        postData["threshold"] = threshold

    if file:
        client.files = {"file": open(file, "rb")}
    else:
        client.files = None
        postData["image_url"] = image_url

    return client.post("https://kapi.kakao.com/v1/vision/product/detect", data=postData)

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def createThumbnail(width, height, file=None, image_url=None):

    postData = {}

    try:
        width = int(width)
    except:
        pass

    if type(width) != int:
        raise AttributeError("[ERROR] width parameter should be int type")

    try:
        height = int(height)
    except:
        pass

    postData["width"] = width
    postData["height"] = height

    if type(height) != int:
        raise AttributeError("[ERROR] height parameter should be int type")

    if file == None and image_url == None:
        raise AttributeError("[ERROR] One of file parameter or image_url parameter is mandatory")
    elif file != None and image_url != None:
        raise AttributeError("[ERROR] Only one of file parameter and image_url parameter can be used")

    if file:
        client.clear_header("Content-Type")
        if type(file) != str:
            raise AttributeError("[ERROR] file parameter should be string type")
        if not os.path.exists(file):
            raise AttributeError("[ERROR] {} file doesn't exist".format(file))
        if not os.access(file, os.R_OK):
            raise AttributeError("[ERROR] Opening {} file is permission denied".format(file))

    if image_url:
        client.clear_header("Content-Type")
        client.set_header("Content-Type", "application/x-www-form-urlencoded")
        if type(image_url) != str:
            raise AttributeError("[ERROR] image_url parameter should be string type")

    if file:
        client.files = {"file": open(file, "rb")}
    else:
        client.files = None
        postData["image_url"] = image_url

    # print(client)

    return client.post("https://kapi.kakao.com/v1/vision/thumbnail/crop", data=postData)

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def detectThumbnail(width, height, file=None, image_url=None):

    postData = {}

    try:
        width = int(width)
    except:
        pass

    if type(width) != int:
        raise AttributeError("[ERROR] width parameter should be int type")

    try:
        height = int(height)
    except:
        pass

    if type(height) != int:
        raise AttributeError("[ERROR] height parameter should be int type")

    postData["width"] = width
    postData["height"] = height

    if file == None and image_url == None:
        raise AttributeError("[ERROR] One of file parameter or image_url parameter is mandatory")
    elif file != None and image_url != None:
        raise AttributeError("[ERROR] Only one of file parameter and image_url parameter can be used")

    if file:
        client.clear_header("Content-Type")
        if type(file) != str:
            raise AttributeError("[ERROR] file parameter should be string type")
        if not os.path.exists(file):
            raise AttributeError("[ERROR] {} file doesn't exist".format(file))
        if not os.access(file, os.R_OK):
            raise AttributeError("[ERROR] Opening {} file is permission denied".format(file))

    if image_url:
        client.clear_header("Content-Type")
        client.set_header("Content-Type", "application/x-www-form-urlencoded")
        if type(image_url) != str:
            raise AttributeError("[ERROR] image_url parameter should be string type")

    if file:
        client.files = {"file": open(file, "rb")}
    else:
        client.files = None
        postData["image_url"] = image_url

    return client.post("https://kapi.kakao.com/v1/vision/thumbnail/detect", data=postData)

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def createMultiTag(file=None, image_url=None):

    postData = {}

    if file == None and image_url == None:
        raise AttributeError("[ERROR] One of file parameter or image_url parameter is mandatory")
    elif file != None and image_url != None:
        raise AttributeError("[ERROR] Only one of file parameter and image_url parameter can be used")

    if file:
        client.clear_header("Content-Type")
        if type(file) != str:
            raise AttributeError("[ERROR] file parameter should be string type")
        if not os.path.exists(file):
            raise AttributeError("[ERROR] {} file doesn't exist".format(file))
        if not os.access(file, os.R_OK):
            raise AttributeError("[ERROR] Opening {} file is permission denied".format(file))

    if image_url:
        client.clear_header("Content-Type")
        client.set_header("Content-Type", "application/x-www-form-urlencoded")
        if type(image_url) != str:
            raise AttributeError("[ERROR] image_url parameter should be string type")

    if file:
        client.files = {"file": open(file, "rb")}
    else:
        client.files = None
        postData["image_url"] = image_url

    return client.post("https://kapi.kakao.com/v1/vision/multitag/generate", data=postData)

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def detectAdultImage(file=None, image_url=None):

    postData = {}

    if file == None and image_url == None:
        raise AttributeError("[ERROR] One of file parameter or image_url parameter is mandatory")
    elif file != None and image_url != None:
        raise AttributeError("[ERROR] Only one of file parameter and image_url parameter can be used")

    if file:
        # client.set_header("Content-Type", "multipart/form-data")
        client.clear_header("Content-Type")
        if type(file) != str:
            raise AttributeError("[ERROR] file parameter should be string type")
        if not os.path.exists(file):
            raise AttributeError("[ERROR] {} file doesn't exist".format(file))
        if not os.access(file, os.R_OK):
            raise AttributeError("[ERROR] Opening {} file is permission denied".format(file))

    if image_url:
        client.clear_header("Content-Type")
        client.set_header("Content-Type", "application/x-www-form-urlencoded")
        if type(image_url) != str:
            raise AttributeError("[ERROR] image_url parameter should be string type")

    if file:
        client.files = {"file": open(file, "rb")}
    else:
        client.files = None
        postData["image_url"] = image_url

    return client.post("https://kapi.kakao.com/v1/vision/adult/detect", data=postData)

"""
    https://developers.kakao.com/docs/restapi/vision
"""
def detectOCR(file):

    if file:
        client.clear_header("Content-Type")
        if type(file) != str:
            raise AttributeError("[ERROR] file parameter should be string type")
        if not os.path.exists(file):
            raise AttributeError("[ERROR] {} file doesn't exist".format(file))
        if not os.access(file, os.R_OK):
            raise AttributeError("[ERROR] Opening {} file is permission denied".format(file))

    if file:
        client.files = {"file": open(file, "rb")}

    # print(client)

    return client.post("https://kapi.kakao.com/v1/vision/text/detect")


"""
    https://developers.kakao.com/docs/restapi/vision
"""
def recognizeOCR(file):
    boxes = detectOCR(file)["result"]["boxes"]

    if boxes != None:
        client.files = {"file": open(file, "rb")}

        postData = {
            "boxes": json.dumps(boxes),
        }

        return client.post("https://kapi.kakao.com/v1/vision/text/recognize", postData)

