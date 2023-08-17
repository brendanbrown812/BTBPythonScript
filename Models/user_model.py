class User:
    def __init__(self, user_data):
        self.user_id = user_data.get("user_id", "N/A")
        self.team_name = user_data.get("metadata", {}).get("team_name", f"Team {user_data.get('display_name', '')}")
        self.display_name = user_data.get("display_name", "N/A")

    def display(self):
        print("User ID:", self.user_id)
        print("Team Name:", self.team_name)
        print("Display Name:", self.display_name)
        print()
