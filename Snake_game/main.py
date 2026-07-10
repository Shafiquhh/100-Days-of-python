
from turtle import Turtle,Screen
import time

from scoreboard import Scoreboard
from food import Food
from snake import Snake
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
food.refresh()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
delay = 0.1
while game_on:
    screen.update()

    time.sleep(delay)
    snake.move()
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.add_segment()
        score.increase_score()
        delay*=0.9
    score.title()
    if snake.head.xcor()>290 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-290:
        score.set_high_score()
        snake.reset()
        delay = 0.1
        # game_on = False
        # score.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.set_high_score()
            snake.reset()
            delay = 0.1
    time.sleep(delay)










screen.exitonclick()