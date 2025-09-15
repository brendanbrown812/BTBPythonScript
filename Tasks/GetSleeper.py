from Tasks.GetSleeperUsers import *
from Tasks.GetNflPlayers import *
from Tasks.GetUserRosters import *
from Tasks.GetSleeperMatchup import *
from Tasks.GetGameHistory import *
from Models.fantasy_team_model import FantasyTeam
from Constants import *

def GetSleeper(week):
    users = GetSleeperUserData()
    rosters = GetUserRosterData()
    players = GetNFLPlayersData()
    matchup_groups = GetSleeperMatchup(week)
    
    fantasy_teams = []
    roster_to_fantasy_team = {}  # Create a dictionary to map roster_id to FantasyTeam
    for roster in rosters:
        owner = next(user for user in users if user.user_id == roster.owner_id)
        fantasy_team = FantasyTeam(owner, roster, players)
        fantasy_teams.append(fantasy_team)
        roster_to_fantasy_team[roster.roster_id] = fantasy_team  # Add the mapping to the dictionary
    
    returnString = ""
    for matchup_group in matchup_groups:
        fantasy_team_1 = roster_to_fantasy_team[matchup_group[0].roster_id]
        fantasy_team_2 = roster_to_fantasy_team[matchup_group[1].roster_id]
        # Look up the historical names from the dictionary and print them
        historical_name_1 = SLEEPER_TO_REAL_NAME.get(fantasy_team_1.user.display_name, fantasy_team_1.user.display_name)
        historical_name_2 = SLEEPER_TO_REAL_NAME.get(fantasy_team_2.user.display_name, fantasy_team_2.user.display_name)

        historical_matchups = GetMatchupHistory(historical_name_1, historical_name_2)
        historical_matchups = sorted(historical_matchups, key=lambda matchup: matchup.Year, reverse=True)

        returnString += f"{historical_name_1} ({fantasy_team_1.user.team_name}) vs. {historical_name_2} ({fantasy_team_2.user.team_name})\n"
        
        for matchup in historical_matchups:
            returnString += f"In {matchup.Year} week {matchup.Week}, {matchup.Winner} won {matchup.Team1Score if matchup.Team1Score > matchup.Team2Score else matchup.Team2Score} to {matchup.Team1Score if matchup.Team1Score < matchup.Team2Score else matchup.Team2Score}{' in a PTGOTW' if matchup.WasPTGOTW == True else ''}\n"
        returnString += "\n"
    return returnString