from turtle import *

SCOREBOARD_POSITION = 200, 280
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.goto(SCOREBOARD_POSITION)
        self.write(f'SCORE: {self.score}', font=FONT)

    def update_score(self):
        self.write(f'SCORE: {self.score}', font=FONT)

