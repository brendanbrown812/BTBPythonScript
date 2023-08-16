import requests
from Models.nfl_player_model import Player

def GetNFLPlayersData(printDisplay=False):
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url)

    if response.status_code == 200:
        players_data = response.json()
        players = [Player(player_id, player_data) for player_id, player_data in players_data.items()]
        for player in players:
            if printDisplay:
                player.display()
    else:
        print(f"Error {response.status_code}: {response.text}")
