from tkinter import *
from quiz_brain import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        correct_image = PhotoImage(file="./images/true.png")
        self.correct = Button(image=correct_image)
        self.correct.grid(row=2,column=0)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=wrong_image)
        self.wrong.grid(row=2,column=1)

        self.score_label = Label(text="Score:", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window,width=300,height=250,bg=THEME_COLOR)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="some questions" ,
                                                     fill = THEME_COLOR,
                                                     font=("Arial",20,"italics")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        self.window.mainloop()




