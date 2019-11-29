from RestClient4py.client import RestClient
from API_Wrap import util
import datetime


api_key = util.youtube_auth()
client = RestClient()

def search(part: str, forContentOwner: bool = None, forMine: bool = None, relatedToVideoId: str = None,
           channelId: str = None, channelType: str = None, eventType: str = None, maxResults: int = 5,
           onBehalfOfContentOwner: str = None, order: str = "relevance", pageToken: str = None,
           publishedAfter: datetime.datetime = None, publishedBefore: datetime.datetime = None, q: str = None,
           regionCode: str = None, safeSearch: str = None, topicId: str = None, type: str = None,
           videoCaption: str = None, videoCategoryId: str = None, videoDefinition: str = None,
           videoDimension: str = None, videoDuration: str = None, videoEmbeddable: str = None, videoLicense: str = None,
           videoSyndicated: str = None, videoType: str = None):

    if part not in ["id", "snippet"]:
        raise AttributeError("[ERROR] part parameter should be one of [id / snippet]")

    if forContentOwner:
        if forMine or relatedToVideoId:
            raise AttributeError("[ERROR] You can use only one filter parameter [forContentOwner / forMine / relatedToVideoId] at once")

    if forMine:
        if forContentOwner or relatedToVideoId:
            raise AttributeError("[ERROR] You can use only one filter parameter [forContentOwner / forMine / relatedToVideoId] at once")
        if not type or type != "video":
            raise AttributeError("[ERROR] When you set forMine parameter as true, you should use type parameter as video")

    if relatedToVideoId:
        if forMine or forContentOwner:
            raise AttributeError("[ERROR] You can use only one filter parameter [forContentOwner / forMine / relatedToVideoId] at once")
        if not type or type != "video":
            raise AttributeError("[ERROR] When you set relatedToVideoId parameter as true, you should use type parameter as video")

    if channelType and channelType not in ["any", "show"]:
        raise AttributeError("[ERROR] channelType parameter should be one of [any / show]")

    if eventType and eventType not in ["completed", "live", "upcoming"]:
        raise AttributeError("[ERROR] eventType parameter should be one of [completed / live / upcoming]")

    if maxResults and (maxResults < 0 or 50 < maxResults):
        raise AttributeError("[ERROR] maxResults parameter should be between 0 ~ 50")

    if order and order not in ["date", "rating", "relevance", "title", "videoCount", "viewCount"]:
        raise AttributeError("[ERROR] order parameter should be one of [date / rating / relevance / title / videoCount / viewCount]")

    if safeSearch and safeSearch not in ["moderate", "none", "strict"]:
        raise AttributeError("[ERROR] safeSearch parameter should be one of [moderate / none / strict]")

    if type and type not in ["channel", "playlist", "video"]:
        raise AttributeError("[ERROR] type parameter should be one of [channel / playlist / video]")

    if videoCaption and videoCaption not in ["any", "closedCaption", "none"]:
        raise AttributeError("[ERROR] videoCaption parameter should be one of [any / closedCaption / none]")

    if videoDefinition and videoDefinition not in ["any", "high", "standard"]:
        raise AttributeError("[ERROR] videoDefinition parameter should be one of [any / high / standard]")

    if videoDimension and videoDimension not in ["2D", "3D", "any"]:
        raise AttributeError("[ERROR] videoDimension parameter should be one of [2D / 3D / any]")

    if videoDuration and videoDuration not in ["any", "long", "medium", "short"]:
        raise AttributeError("[ERROR] videoDuration parameter should be one of [any / long / medium / short]")

    if videoEmbeddable and videoEmbeddable not in ["any", "true"]:
        raise AttributeError("[ERROR] videoEmbeddable parameter should be one of [any / true]")

    if videoLicense and videoLicense not in ["any", "creativeCommon", "youtube"]:
        raise AttributeError("[ERROR] videoLicense parameter should be one of [any / creativeCommon / youtube]")

    if videoSyndicated and videoSyndicated not in ["any", "true"]:
        raise AttributeError("[ERROR] videoSyndicated parameter should be one of [any / true]")

    if videoType and videoType not in ["any", "episode", "movie"]:
        raise AttributeError("[ERROR] videoType parameter should be one of [any / episode / movie]")

    getData = {
        "key": api_key,
        "part": part,
        "forContentOwner": forContentOwner,
        "forMine": forMine,
        "relatedToVideoId": relatedToVideoId,
        "channelId": channelId,
        "channelType": channelType,
        "eventType": eventType,
        "maxResults": maxResults,
        "onBehalfOfContentOwner": onBehalfOfContentOwner,
        "order": order,
        "pageToken": pageToken,
        "publishedAfter": publishedAfter,
        "publishedBefore": publishedBefore,
        "q": q,
        "regionCode": regionCode,
        "safeSearch": safeSearch,
        "topicId": topicId,
        "type": type,
        "videoCaption": videoCaption,
        "videoCategoryId": videoCategoryId,
        "videoDefinition": videoDefinition,
        "videoDimension": videoDimension,
        "videoDuration": videoDuration,
        "videoEmbeddable": videoEmbeddable,
        "videoLicense": videoLicense,
        "videoSyndicated": videoSyndicated,
        "videoType": videoType,
    }

    # print(getData)
    # print(client)
    return client.get("https://www.googleapis.com/youtube/v3/search", params=getData)