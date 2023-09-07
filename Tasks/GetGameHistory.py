from Core import *
from Pages.GameHistoryPage import *
from datetime import datetime

def GetAllGameHistory():
    gameHistoryPages = getGames()

    for game in gameHistoryPages:
        print(f"{game.Year}-{game.Week}-{game.Team1Name}-{game.Team1Score}-{game.Team2Name}-{game.Team2Score}-{game.Winner}-{game.WasPTGOTW}")

def GetMatchupHistory(team1Name, team2Name):
    if not isinstance(team1Name, str):
        raise TypeError("team1Name must be a string.")
    if not isinstance(team2Name, str):
        raise TypeError("team2Name must be a string.")

    gameHistoryPages = getGames()
    # Filter the games based on the team1Name and team2Name parameters
    filtered_games = [game for game in gameHistoryPages if (game.Team1Name == team1Name and game.Team2Name == team2Name) or (game.Team1Name == team2Name and game.Team2Name == team1Name)]

    filtered_games_dict = {}
    for game in filtered_games:
        key = (game.Year, game.Week, game.Team1Name, game.Team2Name)  # Create a unique key based on the attributes of the game
        filtered_games_dict[key] = game

    filtered_games = list(filtered_games_dict.values())

    return filtered_games
    
