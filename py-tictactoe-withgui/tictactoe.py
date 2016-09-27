import copy

class TicTacToe:
    def __init__(self):
        self.current_player = 'X'
        self.game_changed_callback = lambda: None
        self.winner = ''
        self.game_over = False
        self.board = [['' for x in range(3)] for y in range(3)]

    def play(self, x, y):
        if self.board[x][y] == '' and not self.game_over:
            self.board[x][y] = self.current_player
            self.check_game_won()

            if not self.game_over:
                self.toggle_current_player()

            self.game_changed_callback(copy.deepcopy(self.board))
            print(self.board)

    def toggle_current_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_game_won(self):
        if (
            (self.board[0][0] == self.board[0][1] == self.board[0][2] == self.current_player) or
            (self.board[1][0] == self.board[1][1] == self.board[1][2] == self.current_player) or
            (self.board[2][0] == self.board[2][1] == self.board[2][2] == self.current_player) or
            (self.board[0][0] == self.board[1][0] == self.board[2][0] == self.current_player) or
            (self.board[0][1] == self.board[1][1] == self.board[2][1] == self.current_player) or
            (self.board[0][2] == self.board[1][2] == self.board[2][2] == self.current_player) or
            (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player) or
            (self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player)
        ):
            self.game_over = True
            self.winner = self.current_player

    def set_game_changed_callback(self, game_changed_callback):
        self.game_changed_callback = game_changed_callback