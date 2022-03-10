from turtle import Turtle
FONT = ('Courier', 14, 'normal')
ALIGNMENT = 'center'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.show_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def show_score(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER',  align=ALIGNMENT, font=FONT)
