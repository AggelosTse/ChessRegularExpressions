import datetime
import re
import matplotlib.pyplot as plt


def seperategames():
    """seperates the games and appends them in a list"""
    currentgame = ""
    with open(file, encoding="ISO-8859-1") as chess:
        for line in chess:
            line = line.strip()
            if line:
                currentgame += line + "\n"
                if (line.endswith("1-0") or line.endswith("0-1") or line.endswith("1/2-1/2")):
                    games.append(currentgame.strip())
                    currentgame = ""  # Reset currentgame for the next game


def countdays():
    """gets the number of all the days the chess matches took place"""

    weeklist = []
    mond = tuesd = wend = thur = frid = saturd = sund = 0
    for game in games:
        result_pattern = re.compile(r'\[Date "(.*?)"\]')
        match_result = result_pattern.search(game)
        if match_result:
            result_string = match_result.group(1)
        try:
            date = datetime.datetime.strptime(result_string, "%Y.%m.%d")  # converts the date to the specified format.
        except ValueError:
            # Handle cases where date format is different or date is missing
            continue

        weekdays = (date.weekday())  # it finds what day of the week is the date day, and counts it.
        if weekdays == 0:
            mond += 1
        elif weekdays == 1:
            tuesd += 1
        elif weekdays == 2:
            wend += 1
        elif weekdays == 3:
            thur += 1
        elif weekdays == 4:
            frid += 1
        elif weekdays == 5:
            saturd += 1
        else:
            sund += 1

    weeklist = [mond, tuesd, wend, thur, frid, saturd, sund]
    return weeklist


file = "/home/angelo/Downloads/RetiKIA.pgn"
games = []
seperategames()
weekdays = countdays()
days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


plt.bar(days_of_week, weekdays, alpha=0.7)  # it creates the diagram.
plt.xlabel("Days")
plt.ylabel("Matches")
plt.title("Distribution of Matches Played on Each Day of the Week")
plt.show()
