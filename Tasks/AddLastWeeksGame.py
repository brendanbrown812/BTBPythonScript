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

#TO DO
#1. Add logic to email insert statements to Brendan
#2. Send an email to Brendan & Erik when games stop being added.
#3. Send an email to Brendan & Erik when games need to start being added again.

def AddLastWeeksGame():
    load_dotenv()
    addPastGames = os.getenv("ADD_PAST_GAMES")
    if(addPastGames):
        now = datetime.now()
        if now.weekday() == 1:  # Add games on Tuesday morning
            writeupPages = getWriteupPages()
            complete_writeup_pages = [page for page in writeupPages if page.Completed]
            sorted_complete_writeup_pages = sorted(
                complete_writeup_pages,
                key=lambda page: int(page.WeekNumber),
                reverse=True
            )
            writeup_to_add = sorted_complete_writeup_pages[0] if sorted_complete_writeup_pages else None
            
            if writeup_to_add is not None:
                users = GetSleeperUserData()
                rosters = GetUserRosterData()
                players = GetNFLPlayersData()
                matchup_groups = GetSleeperMatchup(writeup_to_add.WeekNumber)
                fantasy_teams = []
                roster_to_fantasy_team = {}  # Create a dictionary to map roster_id to FantasyTeam
                for roster in rosters:
                    owner = next(user for user in users if user.user_id == roster.owner_id)
                    fantasy_team = FantasyTeam(owner, roster, players)
                    fantasy_teams.append(fantasy_team)
                    roster_to_fantasy_team[roster.roster_id] = fantasy_team  # Add the mapping to the dictionary

                for matchup_group in matchup_groups:
                    fantasy_team_1 = roster_to_fantasy_team[matchup_group[0].roster_id]
                    fantasy_team_2 = roster_to_fantasy_team[matchup_group[1].roster_id]
                    # Look up the historical names from the dictionary and print them
                    year = datetime.now().year
                    week = writeup_to_add.WeekNumber
                    team_1_name = SLEEPER_TO_REAL_NAME.get(fantasy_team_1.user.display_name, fantasy_team_1.user.display_name)
                    team_1_score = matchup_group[0].points
                    team_2_name = SLEEPER_TO_REAL_NAME.get(fantasy_team_2.user.display_name, fantasy_team_2.user.display_name)
                    team_2_score = matchup_group[1].points
                    winner = team_1_name
                    if matchup_group[0].points < matchup_group[1].points:
                        winner = team_2_name
                    
                    matchup = MatchupRecord(year, week, team_1_name, team_1_score, team_2_name, team_2_score, winner, False)
                    matchup.InsertGame()
            else:
                # Handle the case where writeup_to_add is None
                print("No writeup to add.")

