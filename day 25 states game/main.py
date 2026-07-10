import turtle
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from email.mime import image

from numpy.core import records

screen = turtle.Screen()
screen.setup(0.50, 0.60)

screen.title("U.S states game")
image = "blank_states_img.gif"


screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


import pandas as pd

data=pd.read_csv("50_states.csv")
Game= True
all_states=data.state.to_list()
pen = turtle.Turtle()
pen.hideturtle()
pen.speed("fastest")

guessed_states=[]
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Your guess: ")
    if answer_state == "" or answer_state is None:
        missing_states=[state for state in all_states if state not in guessed_states]

        for state in missing_states:
            datas=data[data["state"]==state]
            x=datas.x.tolist()
            y=datas.y.tolist()
            pen.speed("fastest")
            pen.up()
            pen.goto(x[0], y[0])
            pen.down()
            pen.color("red")
            pen.circle(1)
            pen.write(state,font=("Arial",8,"normal"))
        break
    answer_state = answer_state.title()
    if answer_state in all_states:

        guessed_states.append(answer_state)
        datas=data[data["state"]==answer_state]
        x=datas.x.tolist()
        y=datas.y.tolist()
        pen.up()
        pen.goto(x[0], y[0])
        pen.down()
        pen.circle(1)

        pen.write(answer_state,font=("Arial",8,"normal"))
    screen.update()


screen.exitonclick()











