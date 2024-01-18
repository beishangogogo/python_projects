import requests
import urllib3
from dotenv import load_dotenv
load_dotenv
import os
import pandas as pd
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

# payload = {
#     'client_id': os.getenv("CLIENT_ID"),
#     'client_secret': os.getenv("CLIENT_SECRET"),
#     'refresh_token': os.getenv("REFRESH_TOKEN"),
#     'grant_type': "refresh_token",
#     'f': 'json'
# }

# print("Requesting Token...\n")
# res = requests.post(auth_url, data=payload, verify=False)
# access_token = res.json().get("access_token")
access_token = "17aae28680ae1da7483f5e7b4e1d435d13cd15e8"
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

data = pd.DataFrame(my_dataset)

data.to_csv('test.csv')
