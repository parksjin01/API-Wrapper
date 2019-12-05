from RestClient4py.client import RestClient
from API_Wrap import util


api_key = util.youtube_auth()
client = RestClient()

"""
    https://developers.google.com/youtube/v3/docs/playlists/list
"""
def list(part:str, channelId:str=None, id:str=None, mine:bool=None, maxResults:int=None, onBehalfOfContentOwner:str=None,
         onBehalfOfContentOwnerChannel:str=None, pageToken:str=None):

    if part not in ["id", "snippet", "status"]:
        raise AttributeError("[ERROR] part parameter should be one of [id / snippet / status]")

    if not channelId and not id and not mine:
        raise AttributeError("[ERROR] One of channelId, id and mine parameter should be used")

    if channelId:
        if id or mine:
            raise AttributeError("[ERROR] Only one of channelId, id or mine parameter should be used")

    if id:
        if channelId or mine:
            raise AttributeError("[ERROR] Only one of channelId, id or mine parameter should be used")

    if mine:
        if channelId or id:
            raise AttributeError("[ERROR] Only one of channelId, id or mine parameter should be used")

    if maxResults and (maxResults < 0 or 50 < maxResults):
        raise AttributeError("[ERROR] maxResults parameter should be between 0 ~ 50")

    getData = {
        "key": api_key,
        "part": part,
        "channelId": channelId,
        "id": id,
        "mine": mine,
        "maxResults": maxResults,
        "onBehalfOfContentOwner": onBehalfOfContentOwner,
        "onBehalfOfContentOwnerChannel": onBehalfOfContentOwnerChannel,
        "pageToken": pageToken
    }

    return client.get("https://www.googleapis.com/youtube/v3/playlists", params=getData)

"""
    https://developers.google.com/youtube/v3/docs/playlists/insert
"""
def insert(part:str):
    """TODO"""

"""
    https://developers.google.com/youtube/v3/docs/playlists/update
"""
def update(part:str):
    """TODO"""

"""
    https://developers.google.com/youtube/v3/docs/playlists/delete
"""
def delete(id:str):
    """TODO"""