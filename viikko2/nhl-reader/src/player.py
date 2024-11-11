import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']

    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} team {self.team}  goals {self.goals} + assists {self.assists}= {self.points}"

class PlayerStats:
    def __init__(self, url):
        self.url = url
        self.players = self.fetch_data()
    
    def fetch_data(self):
        response = requests.get(self.url).json()
        return [Player(player_data) for player_data in response]
    
    def get_finnish_players_sorted(self):
        finnish_players = filter(lambda player: player.nationality == "FIN", self.players)
        return sorted(finnish_players, key=lambda player: player.points, reverse=True)