from turtle import Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time

#
# class line(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.goto(0, 300)
#         for i in range(30):
#             if i % 2 == 0:
#                 self.penup()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()
screen.listen()
screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")
screen.onkey(l_paddle.Up, "w")
screen.onkey(l_paddle.Down, "s")

ball = Ball()
is_game_on = True 
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.restart()
        score.l_point()
    if ball.xcor() < -380:
        ball.restart()
        score.r_point()

screen.exitonclick()
