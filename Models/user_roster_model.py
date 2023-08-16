class Roster:
    def __init__(self, roster_data):
        self.starters = roster_data.get("starters")
        self.settings = roster_data.get("settings")
        self.roster_id = roster_data.get("roster_id")
        self.reserve = roster_data.get("reserve")
        self.players = roster_data.get("players")
        self.owner_id = roster_data.get("owner_id")
        self.league_id = roster_data.get("league_id")

    def display(self):
        print("Owner ID:", f"{self.owner_id}")
        print()
        # Display roster information here (e.g., print to console or save to file)
        pass
