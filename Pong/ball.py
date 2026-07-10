from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()


        self.x_v=10
        self.y_v=10
    def move(self):
        x_cor = self.xcor()+self.x_v
        y_cor = self.ycor()+self.y_v
        self.goto(x_cor,y_cor)

    def bounce_y(self):
        self.y_v*= -1
    def bounce_x(self):
        self.x_v*= -1
    def reset_ball(self):
        self.teleport(0, 0)
        self.bounce_x()




