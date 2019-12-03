from RestClient4py.client import RestClient
from API_Wrap import util


api_key = util.youtube_auth()
client = RestClient()

"""
    https://developers.google.com/youtube/v3/docs/thumbnails/set
"""
def set(videoId:str, onBehalfOfContentOwner:str=None):
    """TODO"""