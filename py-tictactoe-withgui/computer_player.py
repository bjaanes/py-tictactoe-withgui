
class ComputerPlayer:
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def make_play(self):
        if self.two_equal_plays_in_row(0):
            square = self.get_empty_square_in_row(0)
        elif self.two_equal_plays_in_row(1):
            square = self.get_empty_square_in_row(1)
        elif self.two_equal_plays_in_row(2):
            square = self.get_empty_square_in_row(2)
        elif self.two_equal_plays_in_column(0):
            square = self.get_empty_square_in_column(0)
        elif self.two_equal_plays_in_column(1):
            square = self.get_empty_square_in_column(1)
        elif self.two_equal_plays_in_column(2):
            square = self.get_empty_square_in_column(2)
        elif self.two_equal_plays_across_left_to_right():
            square = self.get_empty_square_across_left_to_right()
        elif self.two_equal_plays_across_right_to_left():
            square = self.get_empty_square_across_right_to_left()
        elif self.center_is_free():
            square = 1, 1
        elif self.opponent_has_played_in_corner() and self.get_empty_corner_square() is not None:
            square = self.get_empty_corner_square()
        elif self.no_corner_played():
            square = self.get_empty_corner_square()
        else:
            square = self.get_first_empty_square()

        self.game.play(square[0], square[1])

    def two_equal_plays_in_row(self, row):
        number_of_x = 0
        number_of_o = 0
        current_position = self.game.get_current_position()

        for i in range(3):
            player_in_square = current_position[i][row]
            if player_in_square == 'X':
                number_of_x += 1
            elif player_in_square == 'O':
                number_of_o += 1

        return (number_of_x == 2 and not number_of_o == 1) or (number_of_o == 2 and not number_of_x == 1)

    def two_equal_plays_in_column(self, column):
        number_of_x = 0
        number_of_o = 0
        current_position = self.game.get_current_position()

        for i in range(3):
            player_in_square = current_position[column][i]
            if player_in_square == 'X':
                number_of_x += 1
            elif player_in_square == 'O':
                number_of_o += 1

        return (number_of_x == 2 and not number_of_o == 1) or (number_of_o == 2 and not number_of_x == 1)

    def two_equal_plays_across_left_to_right(self):
        number_of_x = 0
        number_of_o = 0
        current_position = self.game.get_current_position()

        if current_position[0][0] == 'X':
            number_of_x += 1
        if current_position[0][0] == 'O':
            number_of_o += 1
        if current_position[1][1] == 'X':
            number_of_x += 1
        if current_position[1][1] == 'O':
            number_of_o += 1
        if current_position[2][2] == 'X':
            number_of_x += 1
        if current_position[2][2] == 'O':
            number_of_o += 1

        return (number_of_x == 2 and not number_of_o == 1) or (number_of_o == 2 and not number_of_x == 1)

    def two_equal_plays_across_right_to_left(self):
        number_of_x = 0
        number_of_o = 0
        current_position = self.game.get_current_position()

        if current_position[2][0] == 'X':
            number_of_x += 1
        if current_position[2][0] == 'O':
            number_of_o += 1
        if current_position[1][1] == 'X':
            number_of_x += 1
        if current_position[1][1] == 'O':
            number_of_o += 1
        if current_position[0][2] == 'X':
            number_of_x += 1
        if current_position[0][2] == 'O':
            number_of_o += 1

        return (number_of_x == 2 and not number_of_o == 1) or (number_of_o == 2 and not number_of_x == 1)

    def get_empty_square_in_row(self, row):
        current_position = self.game.get_current_position()

        for i in range(3):
            if current_position[i][row] == '':
                return i, row

    def get_empty_square_in_column(self, column):
        current_position = self.game.get_current_position()

        for i in range(3):
            if current_position[column][i] == '':
                return column, i

    def get_empty_square_across_left_to_right(self):
        current_position = self.game.get_current_position()

        if current_position[2][0] == '':
            return 2, 0
        elif current_position[1][1] == '':
            return 1, 1
        elif current_position[0][2] == '':
            return 0, 2

    def get_empty_square_across_right_to_left(self):
        current_position = self.game.get_current_position()

        if current_position[0][2] == '':
            return 0, 2
        elif current_position[1][1] == '':
            return 1, 1
        elif current_position[2][0] == '':
            return 2, 0

    def center_is_free(self):
        current_position = self.game.get_current_position()

        return current_position[1][1] == ''

    def opponent_has_played_in_corner(self):
        current_position = self.game.get_current_position()

        if (
            (current_position[0][0] != '' and current_position[0][0] != self.player) or
            (current_position[2][0] != '' and current_position[2][0] != self.player) or
            (current_position[0][2] != '' and current_position[0][2] != self.player) or
            (current_position[2][2] != '' and current_position[2][2] != self.player)
            ):
            return True
        else:
            return False

    def get_empty_corner_square(self):
        current_position = self.game.get_current_position()

        if current_position[0][0] == '':
            return 0, 0
        elif current_position[2][0] == '':
            return 2, 0
        elif current_position[0][2] == '':
            return 0, 2
        elif current_position[2][2] == '':
            return 2, 2

    def no_corner_played(self):
        current_position = self.game.get_current_position()

        return current_position[0][0] == '' or current_position[2][0] == '' or current_position[0][2] == '' or current_position[2][2] == ''

    def get_first_empty_square(self):
        current_position = self.game.get_current_position()

        for x in range(3):
            for y in range(3):
                if current_position[x][y] == '':
                    return x, y