class Matchup:
    def __init__(self, mathcup_data):
        self.starters = mathcup_data.get("starters", "N/A")
        self.roster_id = mathcup_data.get("roster_id", "N/A")
        self.players = mathcup_data.get("players", "N/A")
        self.matchup_id = mathcup_data.get("matchup_id", "N/A")
        self.points = mathcup_data.get("points", "N/A")
        self.custom_points = mathcup_data.get("custom_points", "N/A")

    def display(self):
        print(f"Roster ID: {self.roster_id}")
        print(f"Points: {self.points}")
        print(f"Matchup ID: {self.matchup_id}")