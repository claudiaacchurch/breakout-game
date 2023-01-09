from turtle import Turtle, Screen

screen = Screen()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.goto(-200, -200)
        self.color("white")
        self.turns = 1

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def keep_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", font=('Courier', 20, ''))

    def show_scores(self):
        self.check_high_score()
        self.write(f"Your score: {self.score}\nHigh score: {self.high_score}\nTurn number: {self.turns}",
                   font=('Courier', 40, ''))

    def continue_game(self):
        self.turns += 1
        self.clear()






