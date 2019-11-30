from RestClient4py.client import RestClient
from API_Wrap import util


api_key = util.youtube_auth()
client = RestClient()

def list(part:str, id:str=None, regionCode:str=None, hl:str="en-US"):

    if part not in ["id", "snippet"]:
        raise AttributeError("[ERROR] part parameter should be one of [id / snippet]")

    if id == None and regionCode == None:
        raise AttributeError("[ERROR] One of id and regionCode parameter must be used")
    if id and regionCode:
        raise AttributeError("[ERROR] Only one of id and regionCode parameter should be used")

    getData = {
        "key": api_key,
        "part": part,
        "id": id,
        "regionCode": regionCode,
        "hl": hl
    }

    return client.get("https://www.googleapis.com/youtube/v3/videoCategories", params=getData)