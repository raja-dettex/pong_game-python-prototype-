from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()

        self.create_paddle(x, y)

    def create_paddle(self, x, y):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.goto(x, y)

    def paddle_move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_move_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
