from Core import *
from decimal import Decimal


class MatchupRecord:
    def __init__(self, year: int, week: int, team1_name: str, team1_score: Decimal, 
                 team2_name: str, team2_score: Decimal, winner: str, was_ptgotw: bool):
        self.year = year
        self.week = week
        self.team_1_name = team1_name
        self.team_1_score = team1_score
        self.team_2_name = team2_name
        self.team_2_score = team2_score
        self.winner = winner
        self.was_ptgotw = was_ptgotw

    def to_dict(self):
        return {
            "year": self.year,
            "week": self.week,
            "team_1_name": self.team_1_name,
            "team_1_score": str(self.team_1_score),  # Convert Decimal to string for JSON
            "team_2_name": self.team_2_name,
            "team_2_score": str(self.team_2_score),  # Convert Decimal to string for JSON
            "winner": self.winner,
            "was_ptgotw": self.was_ptgotw
        }
    
    def InsertGame(self):
        load_dotenv()
        tableId = os.getenv("GAME_HISTORY_PAGE_ID")
        data = {
            "Week": setNotionColumn(NotionColumnType.TITLE, self.week),
            "Year": setNotionColumn(NotionColumnType.NUMBER, self.year),
            "Team1Name": setNotionColumn(NotionColumnType.TEXT, self.team_1_name),
            "Team1Score": setNotionColumn(NotionColumnType.NUMBER, self.team_1_score),
            "Team2Name": setNotionColumn(NotionColumnType.TEXT, self.team_2_name),
            "Team2Score": setNotionColumn(NotionColumnType.NUMBER, self.team_2_score),
            "Winner": setNotionColumn(NotionColumnType.TEXT, self.winner),
            "WasPTGOTW": setNotionColumn(NotionColumnType.CHECKBOX, False)
        }
        insertPage(tableId, data)

    def __str__(self):
        return (f"Year: {self.year}, Week: {self.week}, {self.team_1_name} vs {self.team_2_name}, "
                f"Scores: {self.team_1_score} - {self.team_2_score}, Winner: {self.winner}, "
                f"PTGOTW: {'Yes' if self.was_ptgotw else 'No'}\n")