class GameEntry:
    def __init__(self, user, score):
        self._user = user
        self._score = score

    def get_user(self):
        return self._user

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._user, self._score)

class ScoreBoard:
    """ Fixed length scoreboard of high scores in non ascending order """

    def __init__(self, capacity=5):
        self._board = [None] * capacity
        self._size = 0

    def get_item(self, k):
        return self._board[k]

    def __str__(self):
        return  '\n'.join(str(self._board[j]) for j in range(self._size))

    def add(self, entry):
        """ Entry object is an instance of GameEntry Class  """
        score = entry.get_score()
        good = self._size < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._size < len(self._board):
               self._size += 1
               """ Insert the entry in scoreboard in non-descending order """

            j = self._size - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

if __name__ == "__main__":
    board = ScoreBoard()
    entry = GameEntry('A', 10)
    board.add(entry)
    entry = GameEntry('B', 20)
    board.add(entry)
    entry = GameEntry('C', 15)
    board.add(entry)
    entry = GameEntry('D', 24)
    board.add(entry)
    entry = GameEntry('E', 30)
    board.add(entry)
    entry = GameEntry('F', 99)
    board.add(entry)
    entry = GameEntry('Z', 19)
    board.add(entry)
    print(board)


