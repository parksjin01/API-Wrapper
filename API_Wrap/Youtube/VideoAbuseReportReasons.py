from RestClient4py.client import RestClient
from API_Wrap import util


api_key = util.youtube_auth()
client = RestClient()

"""
    https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list
"""
def list(part:str, hl:str="en-US"):
    """TODO"""