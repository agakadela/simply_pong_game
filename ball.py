""" This module contains the Ball class. """
from turtle import Turtle


class Ball(Turtle):
    """ This class represents the ball."""

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """ Move the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, axis):
        """ Bounce the ball."""
        if axis == 'y':
            self.y_move *= -1
        elif axis == 'x':
            self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """ Reset position of the ball."""
        self.goto(0, 0)
        self.bounce('x')
        self.move_speed = 0.1
