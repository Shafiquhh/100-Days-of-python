import tkinter as tk
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.config(padx=50, pady=10,bg=BACKGROUND_COLOR)
BAR_Y = 460          # vertical position of the bar, below the card
BAR_X_START = 50     # left edge x-coordinate
BAR_X_END = 750       # right edge x-coordinate (full width)
BAR_HEIGHT = 6



canvas = tk.Canvas(width=800,height=530,bg=BACKGROUND_COLOR,highlightthickness=0)
front_photo=tk.PhotoImage(file="./images/card_front.png")
card=canvas.create_image(401,265,image=front_photo)
canvas.grid(row=0,column=0,columnspan=2)
back_photo=tk.PhotoImage(file="./images/card_back.png")
fr_words = pd.read_csv("./data/french_words.csv")
to_learn = fr_words.to_dict(orient="records")
current_card = {}
timer_bar = canvas.create_rectangle(
    BAR_X_START, BAR_Y,
    BAR_X_END, BAR_Y + BAR_HEIGHT,
    fill="white", outline=""
)
def animate_timer_bar(duration_ms=2500, steps=50):
    step_delay = duration_ms // steps
    full_width = BAR_X_END - BAR_X_START
    canvas.itemconfig(timer_bar, fill="black")
    def shrink(step=0):
        if step <= steps:
            remaining_fraction = 1 - (step / steps)
            current_width = full_width * remaining_fraction
            new_x_end = BAR_X_START + current_width
            canvas.coords(timer_bar, BAR_X_START, BAR_Y, new_x_end, BAR_Y + BAR_HEIGHT)
            window.after(step_delay, lambda: shrink(step + 1))

    shrink()
def randomize():
    global current_card,timer
    window.after_cancel(timer)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(text, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=back_photo)
    animate_timer_bar(3000)
    timer = window.after(3000,flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(timer_bar, fill="white")
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(text, text=current_card["French"], font=("arial", 60, "bold"), fill="black")
    canvas.itemconfig(card, image=front_photo)


timer=window.after(100,flip_card)
no_button = tk.PhotoImage(file="./images/wrong.png")
button = tk.Button(image=no_button,bg=BACKGROUND_COLOR,activebackground=BACKGROUND_COLOR,border=0,command=randomize)
button.grid(row=1,column=0)
yes_button = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=yes_button,bg=BACKGROUND_COLOR,activebackground=BACKGROUND_COLOR,border=0,command=randomize)
right_button.grid(row=1,column=1)
lang_text=canvas.create_text(400,150,text="French",font=("arial",40,"italic"))
text=canvas.create_text(400,263,text="",font=("arial",60,"bold"))


window.mainloop()
