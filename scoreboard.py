""" This module contains the Scoreboard class. """
from turtle import Turtle


class Scoreboard(Turtle):
    """ This class represents the scoreball."""

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard(False)

    def update_scoreboard(self, should_show_the_winner=False):
        """ Update the scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center',
                   font=('Arial', 80, 'normal'))
        if should_show_the_winner is True and self.l_score == 10:
            self.goto(-100, 150)
            self.write('You win!', align='center',
                       font=('Arial', 60, 'normal'))

        self.goto(100, 200)
        self.write(self.r_score, align='center',
                   font=('Arial', 80, 'normal'))
        if should_show_the_winner is True and self.r_score == 10:
            self.goto(100, 150)
            self.write('You win!', align='center',
                       font=('Arial', 60, 'normal'))

    def add_point(self, side):
        """ Add point to the proper side"""
        if side == 'l':
            self.l_score += 1
        elif side == 'r':
            self.r_score += 1
        self.update_scoreboard(False)

    def show_the_winner(self):
        """ Showing the winner"""
        self.update_scoreboard(True)
