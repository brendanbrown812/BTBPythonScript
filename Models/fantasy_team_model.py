class FantasyTeam:
    def __init__(self, user, roster, players):
        self.user = user
        self.roster = roster
        self.players = players

    def get_owner(self):
        return self.user
    
    def get_roster(self):
        return self.roster
    
    def get_players(self):
        return self.players
    
    def get_starters(self):
        starters = []
        for player_id in self.roster.starters:
            starters.append(self.players.get(player_id))
        return starters
    
    def get_players(self):
        players = []
        for player_id in self.roster.players:
            players.append(self.players.get(player_id))
        return players
    
    #def get_reserves(self):
        #reserve seems to be empty so we should take players and remove starters from it to get reserve... not sure how to do that :)
    
    def get_team_name(self):
        return self.user.team_name
    
    def get_record(self):
        return f"{self.roster.settings.get('wins', 'N/A')}-{self.roster.settings.get('ties', 'N/A')}-{self.roster.settings.get('losses', 'N/A')}"
    
    def get_wins(self):
        return f"{self.roster.settings.get('wins', 0)}"
    
    def get_ties(self):
        return f"{self.roster.settings.get('ties', 0)}"
    
    def get_losses(self):
        return f"{self.roster.settings.get('losses', 0)}"