import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"

class PlayerStats:
    def __init__(self):
        self.url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
        self.players = []

    def fetch_finnish_players(self):       
        response = requests.get(self.url).json()
        
        for player_dict in response:
            player = Player(player_dict)
            if player.nationality == "FIN":
                self.players.append(player)

    def display_finnish_players(self):

        print("Players from FIN:")
        for player in self.players:
            print(player)