from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.Up,"Up")
screen.onkey(r_paddle.Down,"Down")
screen.onkey(l_paddle.Up,"w")
screen.onkey(l_paddle.Down,"s")

ball = Ball()

is_game_on = True 
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    if (ball.distance(r_paddle) < 70 and ball.xcor() > 340) :
        ball.bounce_x()
    if (ball.distance(l_paddle) < 70 and ball.xcor() < -340) :
        ball.bounce_x()

screen.exitonclick()
