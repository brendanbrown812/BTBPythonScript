import requests
from Models.user_model import User
import os

def GetSleeperUserData(printDisplay=False):
    league_id = os.getenv("SLEEPER_LEAGUE_ID")
    url = f"https://api.sleeper.app/v1/league/{league_id}/users"
    response = requests.get(url)

    if response.status_code == 200:
        users_data = response.json()
        users = [User(user_data) for user_data in users_data]
        for user in users:
            if printDisplay:
                user.display()
    else:
        print(f"Error {response.status_code}: {response.text}")
