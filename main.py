""" This is the main file of the game. """
import functools
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


def paddle_move(direction):
    """ Move the paddle up or down."""
    match direction.lower():
        case "up":
            right_paddle.go_up()
        case "down":
            right_paddle.go_down()
        case "w":
            left_paddle.go_up()
        case "s":
            left_paddle.go_down()


screen.listen()
for k in ['Up', 'Down', 'w', 's']:
    screen.onkeypress(functools.partial(paddle_move, k), key=k)


GAME_IS_ON = True
SPEED = 0.1
while GAME_IS_ON:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')

    if (ball.distance(right_paddle) < 50 and
        ball.xcor() > 320 or
        ball.distance(left_paddle) < 50 and
            ball.xcor() < -320):
        ball.bounce('x')

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_point('l')

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_point('r')
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.show_the_winner()
        GAME_IS_ON = False
screen.exitonclick()
