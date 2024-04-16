from my_re_functions import finddate, findelodifference, findmovesum, findwinner


def seperategames():
    """seperates the games and appends them in a list"""

    currentgame = ""
    with open(file) as chess:
        for line in chess:
            line = line.strip()
            if line:
                currentgame += line + "\n"
                if (line.endswith("1-0") or line.endswith("0-1") or line.endswith("1/2-1/2")):
                    games.append(currentgame.strip())
                    currentgame = ""  # Reset currentgame for the next game


file = "/home/angelo/Downloads/WorldChamp2023.pgn"
games = []
seperategames()
for game in games:
    print(findwinner(game))
    print(findelodifference(game))
    print(finddate(game))
    print(findmovesum(game))
