from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt","r") as file:
            content = file.read()
            self.highscore = int(content)

        self.goto(0, 260)
    def increase_score(self):
        self.score += 1
        self.clear()
    def set_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as file:
                file.write(str(self.score))
        self.score=0
        self.clear()
        self.write(f"Score: {self.score},Highscore:{self.highscore}",align="Center", font=("Courier", 20, "normal"))
    def title(self):
        self.write(f"Score: {self.score},Highscore:{self.highscore}", align="Center", font=("Courier", 20, "normal"))


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Courier", 20, "normal"))

