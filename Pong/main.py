import time
from turtle import Screen,Turtle

from ball import Ball
from paddle import Slider
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
l_slider=Slider(-350)
r_slider=Slider(350)
ball= Ball()
l_slider.color("cyan")
r_slider.color("orange")


screen.listen()

screen.onkeypress(r_slider.move_up,"Up")
screen.onkeypress(r_slider.move_down,"Down")
screen.onkeypress(l_slider.move_up,"w")
screen.onkeypress(l_slider.move_down,"s")
game_is_on=True
l_score=Scoreboard()
r_score=Scoreboard()
l_score.color("cyan")
r_score.color("orange")
l_score.teleport(-280,280)
r_score.teleport(280,280)

timer = 0.1
while game_is_on:

    time.sleep(timer)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_slider) < 50 and ball.xcor()>320 or ball.distance(l_slider) < 50 and ball.xcor()<-320:
        ball.bounce_x()
        timer *= 0.8
    if ball.xcor()>370:
        ball.reset_ball()
        l_score.increase_score()
        l_score.show_score()
        timer = 0.1
    elif ball.xcor()<-370:
        ball.reset_ball()
        r_score.increase_score()
        r_score.show_score()
        timer = 0.1
    l_score.start_score()
    r_score.start_score()


screen.exitonclick()