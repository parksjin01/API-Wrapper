from RestClient4py.client import RestClient
from API_Wrap import util
import pprint
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
                    if type(keyword["keyword"]) != list:
                        raise AttributeError("[ERROR] Value of key `keyword` in keywordGroups parameter should be list of string")
                    for k in keyword["keyword"]:
                        if type(k) != str:
                            raise AttributeError("[ERROR] Value in list of keywordGroups.keyword should be string")
                except:
                    raise AttributeError("[ERROR] Key `keyword` is necessary in element of keywordGroups parameter")

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

    print(client.headers)
    return client.post("https://openapi.naver.com/v1/datalab/search", data=json.dumps(posting_data).encode("utf-8"))


"""
    URL: https://developers.naver.com/products/datalab/
"""
def datalab_shopping():
    """TODO"""

"""
    URL: https://developers.naver.com/products/search/
"""
def searching():
    """TODO"""

"""
    URL: https://developers.naver.com/products/shortenurl/
"""
def shortenURL():
    """TODO"""

"""
    URL: https://developers.naver.com/products/captcha/
"""
def captcha():
    """TODO"""

"""
    URL: https://developers.naver.com/products/navershare/
"""
def naverShare():
    """TODO"""
