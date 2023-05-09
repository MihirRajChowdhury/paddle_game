import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
# Screen related code


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#  paddle related code
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Ball related code
ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the top and bottom wall

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddles

    if ball.distance(l_paddle) <= 50 and ball.xcor() < -320 or ball.distance(r_paddle) <= 50 and ball.xcor() > 320:
        ball.bounce_x()

    # detect collision with lateral walls

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.increase_score(True)

    if ball.xcor() <= -380:
        ball.reset_pos()
        scoreboard.increase_score(False)




screen.exitonclick()
