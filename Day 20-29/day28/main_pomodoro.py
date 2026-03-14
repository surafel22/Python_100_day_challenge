from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canva.itemconfig(timer_text, text = "00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_mark.config(text="")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        timer_label.config(text="BREAK", fg="blue", bg=YELLOW)
        count_down(long_break_sec)
    elif rep % 2 == 0:
        timer_label.config(text="BREAK", fg=RED, bg=YELLOW)
        count_down(short_break_sec)
    else:
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW)
        count_down(work_sec)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canva.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(rep / 2)
        for _ in range(work_session):
            mark = mark + "✅"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canva = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "tomato.png")
canva.create_image(102, 112, image = tomato)
timer_text = canva.create_text(102, 130, text = "00:00", fill="white", font= (FONT_NAME,35 ,"bold"))
canva.grid(row=1, column=1)


timer_label = Label(window, text="Timer", fg= GREEN, bg= YELLOW, font= (FONT_NAME,50))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start",command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=3, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)








window.mainloop()
