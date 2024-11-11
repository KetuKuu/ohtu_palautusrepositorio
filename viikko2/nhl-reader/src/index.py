
from player import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    stats = PlayerStats(url)

    finnish_players = stats.get_finnish_players_sorted()

    print("Players from FIN\n")
    for player in finnish_players:
        print(player)

if __name__ == "__main__":
    main()
