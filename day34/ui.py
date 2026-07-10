from logging import disable
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizUi():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR,padx=20,pady=10)
        self.Canvas=Canvas(width=300,height=250,bg="white")
        self.Canvas.grid(row=1,column=0,columnspan=2)
        self.question_text=self.Canvas.create_text(150,120,width=250,text="rkskngjnfjn",fill="black")
        self.tick_photo=PhotoImage(file="images/true.png")
        self.wrong_photo=PhotoImage(file="images/false.png")
        self.button=Button(image=self.tick_photo,relief="groove",highlightthickness=0,activebackground="black",bg=THEME_COLOR,command=self.correct_answer)
        self.button.grid(row=2,column=1,pady=40)
        self.wrong_answer=Button(image=self.wrong_photo,relief="groove",highlightthickness=0,activebackground="black",bg=THEME_COLOR,command=self.incorrect_answer)
        self.wrong_answer.grid(row=2,column=0,pady=40)
        self.score=Label(text="Score:",font=("impact",16),bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1,pady=20)
        self.get_question()
        self.window.mainloop()
    def get_question(self):
        score = self.quiz.show_score()
        self.Canvas.itemconfig(self.question_text, fill="black")
        self.Canvas.config(bg="white")
        self.score.config(text=f"Score: {score}")
        try:
            q_text=self.quiz.next_question()
            self.Canvas.itemconfig(self.question_text, text=q_text, font=("Arial", 16))
        except IndexError:
            self.Canvas.itemconfig(self.question_text,text=f"You've completed the quiz "
                                                           f" Your final score was: {self.quiz.score}/{self.quiz.question_number}",font=("Arial",16))
            self.button.config(state=DISABLED)
            self.wrong_answer.config(state=DISABLED)
    def correct_answer(self):
        self.feedback(self.quiz.check_answer("True"))
    def incorrect_answer(self):
        self.feedback(self.quiz.check_answer("False"))
    def feedback(self,is_right):
        if is_right:
            self.Canvas.config(bg="green")
            self.Canvas.itemconfig(self.question_text,fill="white")

        else:
            self.Canvas.config(bg="red")
            self.Canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000,self.get_question)





