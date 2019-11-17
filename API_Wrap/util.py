import json
import os

code_path = os.path.dirname(__file__)

def naver_auth():
    with open(code_path + "/config/auth.json") as f:
        auth_data = json.load(f)

    return auth_data["naver"]["client_id"], auth_data["naver"]["client_secret"]