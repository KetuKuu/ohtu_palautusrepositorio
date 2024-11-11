from player import PlayerReader, PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    console = Console()
    season = input("Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/]: ")
    country = input("Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SOL/USA/FIN/GBR/]: ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(country)

    table = Table(title=f"Players from {country}")

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team", justify="center", style="green")
    table.add_column("Goals", justify="center", style="magenta")
    table.add_column("Assists", justify="center", style="magenta")
    table.add_column("Points", justify="center", style="yellow")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    console.print(table)

if __name__ == "__main__":
    main()