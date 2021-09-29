from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x_board, y_board):
        super().__init__()
        self.x = x_board
        self.y = y_board
        self.goto(x_board, y_board)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.write_score()

    def track_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f" score : {self.score}")
