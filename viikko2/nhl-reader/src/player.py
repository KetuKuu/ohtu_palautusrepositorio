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

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player_data) for player_data in response]

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(filtered_players, key=lambda player: player.points, reverse=True)