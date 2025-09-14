from Core import *
from datetime import datetime
from Pages.WriteupPage import *
from Tasks.GetSleeperMatchup import *
from Tasks.GetSleeperUsers import *
from Tasks.GetNflPlayers import *
from Tasks.GetUserRosters import *
from Tasks.GetSleeperMatchup import *
from Tasks.GetGameHistory import *
from Models.fantasy_team_model import FantasyTeam
from Models.notion_game_model import *

def GetWeeklySQL(weekNumber):    
    users = GetSleeperUserData()
    rosters = GetUserRosterData()
    players = GetNFLPlayersData()
    matchup_groups = GetSleeperMatchup(weekNumber)
    fantasy_teams = []
    roster_to_fantasy_team = {}  # Create a dictionary to map roster_id to FantasyTeam
    insertQuery = "INSERT INTO GameHistory (Year, Week, Team1Name, Team1Score, Team2Name, Team2Score, Winner, WasPTGOTW) VALUES "
    for roster in rosters:
        owner = next(user for user in users if user.user_id == roster.owner_id)
        fantasy_team = FantasyTeam(owner, roster, players)
        fantasy_teams.append(fantasy_team)
        roster_to_fantasy_team[roster.roster_id] = fantasy_team  # Add the mapping to the dictionary

    for matchup_group in matchup_groups:
        matchupValues = "("
        fantasy_team_1 = roster_to_fantasy_team[matchup_group[0].roster_id]
        fantasy_team_2 = roster_to_fantasy_team[matchup_group[1].roster_id]
        # Look up the historical names from the dictionary and print them
        year = datetime.now().year
        week = weekNumber
        team_1_name = notion_names.get(fantasy_team_1.user.display_name, fantasy_team_1.user.display_name)
        team_1_score = matchup_group[0].points
        team_2_name = notion_names.get(fantasy_team_2.user.display_name, fantasy_team_2.user.display_name)
        team_2_score = matchup_group[1].points
        winner = team_1_name
        if matchup_group[0].points < matchup_group[1].points:
            winner = team_2_name
        
        matchupValues += f"{year}, {weekNumber}, '{team_1_name}', {team_1_score}, '{team_2_name}', {team_2_score}, '{winner}', 0), "
        insertQuery += matchupValues
    insertQuery = insertQuery[:-2]
    print(insertQuery)

notion_names = {
        "phutt02": "Pete",
        "sasqooch": "Martin",
        "Conman1719": "Conman",
        "bbrown812": "Brendan",
        "AlexKonrardy97": "Ralph",
        "yocool7890": "Bill",
        "erikstacy": "Erik",
        "BigMikeDuzIt": "Diesel",
        "JoHyphenE": "Joey",
        "KurtTruk": "Kurt",
        "Tfugz": "Troy",
        "nbeutin17": "Nate",
    }
    