from turtle import Turtle


class Slider(Turtle):
    def __init__(self,value):
        super().__init__()
        self.shape("square")
        self.turtlesize(5,1)
        self.penup()
        self.teleport(value)
    def move_up(self):
        if self.ycor() < 230:
            self.sety(self.ycor()+20)
    def move_down(self):
        if self.ycor() > -220:
            self.sety(self.ycor()-20)
