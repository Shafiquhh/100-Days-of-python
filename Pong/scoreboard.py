from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
    def increase_score(self):
        self.score += 1
    def show_score(self):

        self.clear()
        self.write(f"Score:{self.score}",align="center",font=("Arial",12,"normal"))
    def start_score(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial", 12, "normal"))
