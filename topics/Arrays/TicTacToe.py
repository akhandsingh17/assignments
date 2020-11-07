"""
Design TicTacToe game which takes move as user input from two users ('X', 'O'). It will keep track of the moves and report
a winner, but it does not perform any strategy or allow someone to play Tic-Tac-Toe against the computer.
"""

class TicTacToe:
    " nested non-public class board to maintain a 3x3 matrix "
    def __init__(self):
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'

    def __str__(self):
        rows = ['|'.join(self._board[j]) for j in range(3)]
        return '\n------\n'.join(rows)

    def mark(self, i, j):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position already occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def is_win(self, mark):
        """ Check board configuration for each move to decide the winner """
        board = self._board
        return (
            mark == board[0][0] == board[0][1] == board[0][2] or
            mark == board[1][0] == board[1][1] == board[1][2] or
            mark == board[2][0] == board[2][1] == board[2][2] or
            mark == board[0][0] == board[1][0] == board[2][0] or
            mark == board[0][1] == board[1][1] == board[2][1] or
            mark == board[0][2] == board[1][2] == board[2][2] or
            mark == board[0][0] == board[1][1] == board[2][2] or
            mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        """ Return the mark of the winning player otherwise return None """
        for mark in 'XO':
            if self.is_win(mark):
                return mark
        return None

if __name__ == "__main__":
    game = TicTacToe()
    game.mark(1, 1)
    game.mark(0, 2)
    game.mark(2, 2)
    game.mark(0, 0)
    game.mark(1, 2)
    game.mark(1, 0)
    game.mark(2, 0)
    game.mark(0, 1)
    print(game)
    winner = game.winner()
    if winner is None:
        print("Tie")
    else:
        print(winner, "won the game !")
