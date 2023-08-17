import requests
from Models.user_roster_model import Roster
import os

def GetUserRosterData():
    league_id = os.getenv("SLEEPER_LEAGUE_ID")
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    response = requests.get(url)

    if response.status_code == 200:
        rosters_data = response.json()
        rosters = [Roster(roster_data) for roster_data in rosters_data]
        return rosters
    else:
        print(f"Error {response.status_code}: {response.text}")
