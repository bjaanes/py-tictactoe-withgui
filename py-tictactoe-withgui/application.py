import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QMessageBox, QApplication)
from PyQt5.QtCore import (QSize)
from tictactoe import TicTacToe
from computer_player import ComputerPlayer


class Main(QWidget):

    def __init__(self, game):
        super().__init__()
        self.game_done = False
        self.grid = QGridLayout()
        self.buttons = [['' for x in range(3)] for y in range(3)]
        self.game = game
        self.computer = ComputerPlayer(game, 'O')
        self.initUI()

        game.set_game_changed_callback(lambda current_position: self.update_ui(current_position))
        game.set_game_won_callback(lambda winner: self.announce_winner(winner))

    def initUI(self):
        self.setLayout(self.grid)

        self.add_button(0, 0)
        self.add_button(0, 1)
        self.add_button(0, 2)
        self.add_button(1, 0)
        self.add_button(1, 1)
        self.add_button(1, 2)
        self.add_button(2, 0)
        self.add_button(2, 1)
        self.add_button(2, 2)

        restart_button = QPushButton("Restart Game")
        restart_button.clicked.connect(lambda: self.restart_game())
        self.grid.addWidget(restart_button, 3, 0, 1, 3)

        self.move(300, 150)
        self.setWindowTitle('Py Tic Tac Toe')
        self.show()

    def update_ui(self, current_position):
        for x in range(len(current_position)):
            for y in range(len(current_position[x])):
                self.buttons[x][y].setText(current_position[x][y])

    def add_button(self, x, y):
        button = self.create_button(x, y)
        self.buttons[x][y] = button
        self.grid.addWidget(button, x, y)

    def create_button(self, x, y):
        button = QPushButton("")
        button.setFixedSize(QSize(100, 100))
        button.clicked.connect(lambda: self.make_player_move(x, y))

        return button

    def make_player_move(self, x, y):
        if self.buttons[x][y].text() == '':
            self.game.play(x, y)
            if not self.game_done:
                self.computer.make_play()

    def restart_game(self):
        self.game.restart()
        self.game_done = False

    def announce_winner(self, winner):
        self.game_done = True
        msg = QMessageBox(self)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle("Game Done!")

        if winner == '':
            msg.setText("It was a Draw!")
        else:
            msg.setText("The winner was " + winner + "!")

        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    ex = Main(game)
    sys.exit(app.exec_())
