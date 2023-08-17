from Core import *
from Pages.GameHistoryPage import *
from datetime import datetime

def GetHameHistory():
    gameHistoryPages = getGames()

    for game in gameHistoryPages:
        print(f"{game.Year}-{game.Week}-{game.Team1Name}-{game.Team1Score}-{game.Team2Name}-{game.Team2Score}-{game.Winner}-{game.WasPTGOTW}")