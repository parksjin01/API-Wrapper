from RestClient4py.client import RestClient
from API_Wrap import util


api_key = util.youtube_auth()
client = RestClient()

def set(channelId:str, onBehalfOfContentOwner:str=None):
    """TODO"""

def unset(channelId:str, onBehalfOfContentOwner:str=None):
    """TODO"""