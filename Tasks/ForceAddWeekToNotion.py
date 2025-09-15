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

def ForceAddWeekToNotion(weekNumber):
    try:
        week_str = str(weekNumber)
        
        users = GetSleeperUserData()
        rosters = GetUserRosterData()
        players = GetNFLPlayersData()
        matchup_groups = GetSleeperMatchup(week_str)
        
        fantasy_teams = []
        roster_to_fantasy_team = {} 
        
        for roster in rosters:
            owner = next(user for user in users if user.user_id == roster.owner_id)
            fantasy_team = FantasyTeam(owner, roster, players)
            fantasy_teams.append(fantasy_team)
            roster_to_fantasy_team[roster.roster_id] = fantasy_team

        games_added = 0
        for matchup_group in matchup_groups:
            fantasy_team_1 = roster_to_fantasy_team[matchup_group[0].roster_id]
            fantasy_team_2 = roster_to_fantasy_team[matchup_group[1].roster_id]
            
            year = datetime.now().year
            week = week_str
            team_1_name = SLEEPER_TO_REAL_NAME.get(fantasy_team_1.user.display_name, fantasy_team_1.user.display_name)
            team_1_score = matchup_group[0].points
            team_2_name = SLEEPER_TO_REAL_NAME.get(fantasy_team_2.user.display_name, fantasy_team_2.user.display_name)
            team_2_score = matchup_group[1].points
            
            winner = team_1_name
            if matchup_group[0].points < matchup_group[1].points:
                winner = team_2_name
            
            matchup = MatchupRecord(year, week, team_1_name, team_1_score, team_2_name, team_2_score, winner, False)
            matchup.InsertGame()
            games_added += 1
            
            print(f"Added game: {team_1_name} ({team_1_score}) vs {team_2_name} ({team_2_score}) - Winner: {winner}")
        
        print(f"Successfully added {games_added} games for Week {week_str} to Notion.")
        
    except Exception as e:
        print(f"Error adding Week {weekNumber} to Notion: {str(e)}")
        raise