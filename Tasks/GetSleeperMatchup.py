import requests
from Models.matchup_model import Matchup
import os
from collections import defaultdict

def GetSleeperMatchup(week=1):
    league_id = os.getenv("SLEEPER_LEAGUE_ID")
    url = f"https://api.sleeper.app/v1/league/{league_id}/matchups/{week}"
    response = requests.get(url)

    if response.status_code == 200:
        matchup_data = response.json()
        
        # Create a dictionary to group Matchup objects by their matchup_id
        grouped_matchups = defaultdict(list)
        
        # Create Matchup objects and add them to the dictionary
        for item in matchup_data:
            matchup = Matchup(item)
            grouped_matchups[matchup.matchup_id].append(matchup)
        
        # Convert the dictionary values to a list of lists
        return list(grouped_matchups.values())
    else:
        print(f"Error {response.status_code}: {response.text}")