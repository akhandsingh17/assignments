"""
Q: Given a table which has three columns for home team, away team and winner and data for a 3 team tournament, create a scorecard such that:
--Input
Home, away, winner
A, B, A
A, C, A
B, C, B
B, A, NULL
C, A, C
C, B, C


--Scorecard

W = 3
T/D = 1
L = 0

--Output
Team, Played, Wins, Losses, Ties, Points
A, 4, 2, 1, 1, 7
B, 4..
C, 4..
"""

from collections import defaultdict



class ScoreEntry:
    def __init__(self, no_of_teams):
        self.team_count = no_of_teams
        self.scorebaord = []

    class ScoreCard:
        def __init__(self, win=3, draw=1, loose=0):
            self.win = int(win)
            self.draw = int(draw)
            self.loose = int(loose)

        def get_win_point(self):
            return self.win

        def get_draw_point(self):
            return self.draw

        def get_loose_point(self):
            return self.loose

    class GameEntry:
        def __init__(self, home, away, winner):
            self.home = home
            self.away = away
            self.winner = winner

    def game_entry(self, home, away, winner):
        self.scorebaord.append(self.GameEntry(home, away, winner))

    def get_score_board(self):
        scorecard = self.ScoreCard()
        dd = defaultdict(list)
        for score_entry in self.scorebaord:
            if score_entry.home == score_entry.winner:
               # Played, Wins, Losses, Ties, Points
                wins = scorecard.get_win_point()
                dd[score_entry.home].append([wins, 0, 0])
            elif score_entry.winner is None:
                ties = scorecard.get_draw_point()
                dd[score_entry.home].append([0, 0, ties])
                dd[score_entry.away].append([0, 0, ties])
            else:
                dd[score_entry.home].append([0, 0, 0])

        for key, values in dd.items():
            print(key, sum([sum(value) for value in values]))


if __name__ == "__main__":
    s = ScoreEntry(3)
    s.game_entry('A', 'B', 'A')
    s.game_entry('A', 'C', 'A')
    s.game_entry('B', 'C', 'B')
    s.game_entry('B', 'A', None)
    s.game_entry('C', 'A', 'C')
    s.game_entry('C', 'B', 'C')
    print(s.get_score_board())
