from RestClient4py.client import RestClient
from API_Wrap import util


api_key = util.youtube_auth()
client = RestClient()

"""
    https://developers.google.com/youtube/v3/docs/subscriptions/list
"""
def list(part:str, channelId:str=None, id:str=None, mine:bool=None, mySubscribers:bool=None, forChannelId:str=None,
         maxResults:int=5, onBehalfOfContentOwner:str=None, onBehalfOfContentOwnerChannel:str=None, order:str="relevance",
         pageToken:str=None):

    if part not in ["id", "snippet", "contentDetails"]:
        raise AttributeError("[ERROR] part parameter should be one of [id / snippet / contentDetails]")

    if channelId == None and id == None and mine == None and mySubscribers == None:
        raise AttributeError("[ERROR] One of channelId, id, mine and mySubscribers parameter should be used")

    if channelId:
        if id or mine or mySubscribers:
            raise AttributeError("[ERROR] Only one of channelId, id, mine and mySubscribers parameter should be used")

    if id:
        if channelId or mine or mySubscribers:
            raise AttributeError("[ERROR] Only one of channelId, id, mine and mySubscribers parameter should be used")

    if mine:
        if channelId or id or mySubscribers:
            raise AttributeError("[ERROR] Only one of channelId, id, mine and mySubscribers parameter should be used")

    if mySubscribers:
        if channelId or id or mine:
            raise AttributeError("[ERROR] Only one of channelId, id, mine and mySubscribers parameter should be used")

    if maxResults and (maxResults < 0 or 50 < maxResults):
        raise AttributeError("[ERROR] maxResults parameter should be between 0 ~ 50")

    if order and order not in ["alphabetical", "relevance", "unread"]:
        raise AttributeError("[ERROR] order parameter should be one of [alphabetical / relevance / unread]")

    getData = {
        "key": api_key,
        "part": part,
        "channelId": channelId,
        "id": id,
        "mine": mine,
        "mySubscribers": mySubscribers,
        "forChannelId": forChannelId,
        "maxResults": maxResults,
        "onBehalfOfContentOwner": onBehalfOfContentOwner,
        "onBehalfOfContentOwnerChannel": onBehalfOfContentOwnerChannel,
        "order": order,
        "pageToken": pageToken
    }

    return client.get("https://www.googleapis.com/youtube/v3/subscriptions", params=getData)

"""
    https://developers.google.com/youtube/v3/docs/subscriptions/insert
"""
def insert(part:str):

    if part not in ["snippet", "contentDetails"]:
        raise AttributeError("[ERROR] part parameter should be one of [snippet / contentDetails]")

    """TODO"""

"""
    https://developers.google.com/youtube/v3/docs/subscriptions/delete
"""
def delete(id:str):
    """TODO"""