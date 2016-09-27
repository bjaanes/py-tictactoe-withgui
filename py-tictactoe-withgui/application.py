
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)
from PyQt5.QtCore import (QSize)
from tictactoe import TicTacToe


class Example(QWidget):

    def __init__(self, game):
        super().__init__()
        self.buttons = [['' for x in range(3)] for y in range(3)]
        self.game = game
        self.initUI()
        game.set_game_changed_callback(lambda current_position: self.update_ui(current_position))

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.addButton(0, 0)
        self.addButton(0, 1)
        self.addButton(0, 2)
        self.addButton(1, 0)
        self.addButton(1, 1)
        self.addButton(1, 2)
        self.addButton(2, 0)
        self.addButton(2, 1)
        self.addButton(2, 2)


        self.move(300, 150)
        self.setWindowTitle('Py Tic Tac Toe')
        self.show()

    def update_ui(self, current_position):
        for x in range(len(current_position)):
            for y in range(len(current_position[x])):
                self.buttons[x][y].setText(current_position[x][y])



    def addButton(self, x, y):
        button = self.createButton(x, y)
        self.buttons[x][y] = button
        self.grid.addWidget(button, x, y)

    def createButton(self, x, y):
        button = QPushButton("")
        button.setFixedSize(QSize(100, 100))
        button.clicked.connect(lambda: self.game.play(x, y))

        return button



if __name__ == '__main__':

    app = QApplication(sys.argv)
    game = TicTacToe()
    ex = Example(game)
    sys.exit(app.exec_())