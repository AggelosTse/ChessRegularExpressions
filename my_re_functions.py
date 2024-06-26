import re

def findwinner(match):
    """returns draw,black or white according to the result of the match"""

    result_pattern = re.compile(r'\[Result "(.*?)"\]')  # im giving it a pattern to search for.
    match_result = result_pattern.search(match)  # im searching for that pattern in the match.
    if match_result:
        result_string = match_result.group(1)  # takes the expression.
        if result_string == "1/2-1/2":
            return "Draw"
        elif result_string == "1-0":
            return "White"
        elif result_string == "0-1":
            return "Black"
        else:
            print("Invalid game result format")
    else:
        print("Invalid game result format")


def findelodifference(match):
    """returns the elo difference from the 2 players"""

    result_pattern1 = re.compile(r'\[WhiteElo "(.*?)"\]')
    match_result1 = result_pattern1.search(match)
    if match_result1:
        result_string1 = match_result1.group(1)

    result_pattern2 = re.compile(r'\[BlackElo "(.*?)"\]')
    match_result2 = result_pattern2.search(match)
    if match_result2:
        result_string2 = match_result2.group(1)

    return abs(int(result_string1) - int(result_string2))


def finddate(match):
    """returns the date on which the match was played"""

    result_pattern = re.compile(r'\[Date "(.*?)"\]')
    match_result = result_pattern.search(match)
    if match_result:
        result_string = match_result.group(1)

    datelist = result_string.split(".")  # splits the date into a 3 length list.
    temp = datelist[0]
    datelist[0] = datelist[2]
    datelist[2] = temp  # reverses the list so that the date displays in the correct format.

    formatted_date_str = ".".join(datelist)
    return formatted_date_str


def findmovesum(match):
    """returns the number of moves played in the match"""

    move_pattern = re.compile(r"\b\d+\.\s*([NBRQK]?[a-h]?[1-8]?x?[a-h][1-8](=[NBRQ])?[+#]?|-{1,2}|O-O(-O)?)\b")
    moves = move_pattern.findall(match)  # Find all move notations
    move_count = len(moves)

    return move_count


chessmatch = """[Event "WCh 2023"]
[Site "Astana KAZ"]
[Date "2023.04.09"]
[Round "1.1"]
[White "Nepomniachtchi,I"]
[Black "Ding Liren"]
[Result "1/2-1/2"]
[WhiteElo "2795"]
[BlackElo "2788"]
[ECO "C85"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Bxc6 dxc6 7.Re1 Nd7 8.d4 exd4
9.Qxd4 O-O 10.Bf4 Nc5 11.Qe3 Bg4 12.Nd4 Qd7 13.Nc3 Rad8 14.Nf5 Ne6 15.Nxe7+ Qxe7
16.Bg3 Bh5 17.f3 f6 18.h3 h6 19.Kh2 Bf7 20.Rad1 b6 21.a3 a5 22.Ne2 Rxd1 23.Rxd1 Rd8
24.Rd3 c5 25.Qd2 c6 26.Rxd8+ Nxd8 27.Qf4 b5 28.Qb8 Kh7 29.Bd6 Qd7 30.Ng3 Ne6
31.f4 h5 32.c3 c4 33.h4 Qd8 34.Qb7 Be8 35.Nf5 Qd7 36.Qb8 Qd8 37.Qxd8 Nxd8
38.Nd4 Nb7 39.e5 Kg8 40.Kg3 Bd7 41.Bc7 Nc5 42.Bxa5 Kf7 43.Bb4 Nd3 44.e6+ Bxe6
45.Nxc6 Bd7 46.Nd4 Nxb2 47.Kf3 Nd3 48.g3 Nc1 49.Ke3 1/2-1/2"""

if __name__ == "__main__":

    print(findwinner(chessmatch))
    print(findelodifference(chessmatch))
    print(finddate(chessmatch))
    print(findmovesum(chessmatch))
