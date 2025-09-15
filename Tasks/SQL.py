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
from Constants import *

def GetWeeklySQL(weekNumber):    
    users = GetSleeperUserData()
    rosters = GetUserRosterData()
    players = GetNFLPlayersData()
    matchup_groups = GetSleeperMatchup(weekNumber)
    fantasy_teams = []
    roster_to_fantasy_team = {}
    insertQuery = "INSERT INTO GameHistory (Year, Week, Team1Name, Team1Score, Team2Name, Team2Score, Winner, WasPTGOTW) VALUES \n"
    for roster in rosters:
        owner = next(user for user in users if user.user_id == roster.owner_id)
        fantasy_team = FantasyTeam(owner, roster, players)
        fantasy_teams.append(fantasy_team)
        roster_to_fantasy_team[roster.roster_id] = fantasy_team

    for matchup_group in matchup_groups:
        matchupValues = "("
        fantasy_team_1 = roster_to_fantasy_team[matchup_group[0].roster_id]
        fantasy_team_2 = roster_to_fantasy_team[matchup_group[1].roster_id]
        
        year = datetime.now().year
        week = weekNumber
        team_1_name = SLEEPER_TO_REAL_NAME.get(fantasy_team_1.user.display_name, fantasy_team_1.user.display_name)
        team_1_score = matchup_group[0].points
        team_2_name = SLEEPER_TO_REAL_NAME.get(fantasy_team_2.user.display_name, fantasy_team_2.user.display_name)
        team_2_score = matchup_group[1].points
        winner = team_1_name
        if matchup_group[0].points < matchup_group[1].points:
            winner = team_2_name
        
        matchupValues += f"{year}, {weekNumber}, '{team_1_name}', {team_1_score}, '{team_2_name}', {team_2_score}, '{winner}', 0), \n"
        insertQuery += matchupValues
    insertQuery = insertQuery[:-3]
    print(insertQuery)
    