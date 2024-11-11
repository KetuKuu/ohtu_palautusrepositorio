
from player import PlayerStats

def main():

    stats = PlayerStats()
    stats.fetch_finnish_players()
    stats.display_finnish_players()

if __name__ == "__main__":
    main()
