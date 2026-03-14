from tkinter import *

window = Tk()
window.title("my first gui program")
window.minsize(400, 400)
window.config(padx=100, pady=200)

my_label = Label(text="yeehoo", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)
def label():
    my_label.config(text="new text")


def button_clicked():
    word = input.get()
    my_label["text"]= word

button = Button(text = "click me", command = button_clicked)
button.grid(column=1, row=1)

new_button = Button(text ="click there",command = label)
new_button.grid(column = 2, row = 1)

input = Entry()
input.grid(column=3, row=3)

window.mainloop()