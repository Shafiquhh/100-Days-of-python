import turtle
from turtle import Turtle
import random
turtle.colormode(255)
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        x_value = 0
        for pos in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.setx(x_value)
            x_value -= 20
            self.segments.append(tim)
    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
    def reset(self):
        for segment in self.segments:
            segment.teleport(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
    def move(self):
            for seg_num in range(len(self.segments) - 1, 0, -1):
                x_cor = self.segments[seg_num - 1].xcor()
                y_cor = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(x_cor, y_cor)

            self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


