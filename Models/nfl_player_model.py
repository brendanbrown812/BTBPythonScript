class Player:
    def __init__(self, player_id, player_data):
        self.player_id = player_id
        self.hashtag = player_data.get("hashtag")
        self.depth_chart_position = player_data.get("depth_chart_position")
        self.status = player_data.get("status")
        self.sport = player_data.get("sport")
        self.fantasy_positions = player_data.get("fantasy_positions")
        self.number = player_data.get("number")
        self.search_last_name = player_data.get("search_last_name")
        self.injury_start_date = player_data.get("injury_start_date")
        self.weight = player_data.get("weight")
        self.position = player_data.get("position")
        self.practice_participation = player_data.get("practice_participation")
        self.sportradar_id = player_data.get("sportradar_id")
        self.team = player_data.get("team")
        self.last_name = player_data.get("last_name")
        self.college = player_data.get("college")
        self.fantasy_data_id = player_data.get("fantasy_data_id")
        self.injury_status = player_data.get("injury_status")
        self.height = player_data.get("height")
        self.search_full_name = player_data.get("search_full_name")
        self.age = player_data.get("age")
        self.stats_id = player_data.get("stats_id")
        self.birth_country = player_data.get("birth_country")
        self.espn_id = player_data.get("espn_id")
        self.search_rank = player_data.get("search_rank")
        self.first_name = player_data.get("first_name")
        self.depth_chart_order = player_data.get("depth_chart_order")
        self.years_exp = player_data.get("years_exp")
        self.rotowire_id = player_data.get("rotowire_id")
        self.rotoworld_id = player_data.get("rotoworld_id")
        self.search_first_name = player_data.get("search_first_name")
        self.yahoo_id = player_data.get("yahoo_id")

    def display(self):
        print("Name:", f"{self.first_name} {self.last_name} Position: {self.position}")
