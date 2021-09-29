import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from wall import Wall

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()

screen.listen()
wall = Wall()
l_scoreboard = Scoreboard(-200, 280)
r_scoreboard = Scoreboard(200, 280)




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)


    screen.onkey(l_paddle.paddle_move_up, "Up")
    screen.onkey(l_paddle.paddle_move_down, "Left")
    screen.onkey(r_paddle.paddle_move_up, "Right")
    screen.onkey(r_paddle.paddle_move_down, "Down")

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 315:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -315:
        ball.bounce_x()

    if ball.xcor() == 330:
        l_scoreboard.track_score()
        ball.move()

    if ball.xcor() == -330:
        r_scoreboard.track_score()
        ball.move()















screen.exitonclick()