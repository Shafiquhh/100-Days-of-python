from turtle import Turtle
import random
coord=[]
for i in range(-280,281,20):
    coord.append(i)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.shapesize(0.98)
        self.speed("fastest")

    def refresh(self):
        rand_x=random.choice(coord)
        rand_y=random.choice(coord)
        self.setx(rand_x)
        self.sety(rand_y)

