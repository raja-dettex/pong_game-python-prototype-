from turtle import Turtle


class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.create_wall()

    def create_wall(self):
        self.shape("square")
        self.shapesize(30, 0.5)
        self.color("blue")
        self.penup()
