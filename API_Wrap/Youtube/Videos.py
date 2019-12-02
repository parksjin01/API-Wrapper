from RestClient4py.client import RestClient
from API_Wrap import util


api_key = util.youtube_auth()
client = RestClient()

def list(part:str, chart:str=None, id:str=None, myRating:str=None, maxResults:int=5, onBehalfOfContentOwner:str=None,
         pageToken:str=None, regionCode:str=None, videoCategoryId:str=None):

    if part not in ["id", "snippet", "contentDetails", "fileDetails", "liveStreamingDetails", "player",
                    "processingDetails", "recordingDetails", "statistics", "status", "suggestions", "topicDetails"]:
        raise AttributeError("[ERROR] part parameter should be one of [id / snippet / contentDetails / fileDetails /"
                             " liveStreamingDetails / player / processingDetails / recordingDetails / statistics / "
                             "status / suggestions / topicDetails")

    if chart == None and id == None and myRating == None:
        raise AttributeError("[ERROR] One of chart, id and myRating parameter should be used")

    if chart and chart != "mostPopular":
        raise AttributeError("[ERROR] chart parameter should be mostPopular")

    if myRating and myRating not in ["like", "dislike"]:
        raise AttributeError("[ERROR] myRating parameter should be one of [like / dislike]")

    if maxResults and (maxResults < 0 or 50 < maxResults):
        raise AttributeError("[ERROR] maxResults parameter should be between 0 ~ 50")

    if videoCategoryId:
        if chart == None:
            raise AttributeError("[ERROR] videoCategoryId parameter can be used when chart parameter is used")

    getData = {
        "key": api_key,
        "part": part,
        "chart": chart,
        "id": id,
        "myRating": myRating,
        "maxResults": maxResults,
        "onBehalfOfContentOwner": onBehalfOfContentOwner,
        "pageToken": pageToken,
        "regionCode": regionCode,
        "videoCategoryId": videoCategoryId
    }

    return client.get("https://www.googleapis.com/youtube/v3/videos", params=getData)

def insert(part:str, autoLevels:bool=None, onBehalfOfContentOwner:str=None, onBehalfOfContentOwnerChannel:str=None,
           stabilize:bool=None):

    if part not in ["id", "snippet", "contentDetails", "fileDetails", "liveStreamingDetails", "player",
                    "processingDetails", "recordingDetails", "statistics", "status", "suggestions", "topicDetails"]:
        raise AttributeError("[ERROR] part parameter should be one of [id / snippet / contentDetails / fileDetails /"
                             " liveStreamingDetails / player / processingDetails / recordingDetails / statistics / "
                             "status / suggestions / topicDetails")

    """TODO"""

def update(part:str, onBehalfOfContentOwner:str=None):

    if part not in ["id", "snippet", "contentDetails", "fileDetails", "liveStreamingDetails", "player",
                    "processingDetails", "recordingDetails", "statistics", "status", "suggestions", "topicDetails"]:
        raise AttributeError("[ERROR] part parameter should be one of [id / snippet / contentDetails / fileDetails /"
                             " liveStreamingDetails / player / processingDetails / recordingDetails / statistics / "
                             "status / suggestions / topicDetails")

    """TODO"""

def rate(id:str, rating:str, onBehalfOfContentOwner:str=None):

    if rating not in ["like", "dislike", "none"]:
        raise AttributeError("[ERROR] rating parameter should be one of [like / dislike / none]")

    """TODO"""

def getRating(id:str, onBehalfOfContentOwner:str=None):
    """TODO"""

def reportAbuse(onBehalfOfContentOwner:str=None):
    """TODO"""

def delete(id:str, onBehalfOfContentOwner:str=None):
    """TODO"""

