from Tasks.GetSleeperUsers import *
from Tasks.GetNflPlayers import *
from Tasks.GetUserRosters import *
from Models.fantasy_team_model import FantasyTeam

def GetSleeper():
    users = GetSleeperUserData()
    rosters = GetUserRosterData()
    players = GetNFLPlayersData()
    
    fantasy_teams = []
    for roster in rosters:
        owner = next(user for user in users if user.user_id == roster.owner_id)
        fantasy_teams.append(FantasyTeam(owner, roster, players))
    
    for team in fantasy_teams:
        print(f"Team Name: {team.get_team_name()}")
        print(f"Owner: {team.get_owner().display_name}")
        print("Starters:")
        for player in team.get_starters():
            print(f"{player.first_name if player and player.first_name else 'N/A'} {player.last_name if player and player.last_name else 'N/A'} ({player.position if player and player.position else 'N/A'})")
        print(f"Record: {team.get_record()}")
        print()

    return fantasy_teams