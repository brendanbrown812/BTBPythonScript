class Roster:
    def __init__(self, roster_data):
        self.starters = roster_data.get("starters", "N/A")
        self.settings = roster_data.get("settings", "N/A")
        self.roster_id = roster_data.get("roster_id", "N/A")
        self.players = roster_data.get("players", "N/A")
        self.owner_id = roster_data.get("owner_id", "N/A")
        self.league_id = roster_data.get("league_id", "N/A")
        #self.reserve = roster_data.get("reserve")
        #reserve seems to be empty so we should take players and remove starters from it to get reserve... not sure how to do that :)

    def display(self):
        print("Owner ID:", f"{self.owner_id}")
        print()
        # Display roster information here (e.g., print to console or save to file)
        pass
