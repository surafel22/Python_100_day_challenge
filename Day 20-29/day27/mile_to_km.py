from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300, 100)
window.config(padx=20, pady=20)

def calculate():
    mile = miles.get()
    km = float(mile) * 1.60934
    km_label["text"] = f"is equal to: {km} km"
miles = Entry(width=7)
miles.grid(row=0, column=1)

mile_label = Label(text="  Miles", fg="red", font=("Arial", 15))
mile_label.grid(row=0, column=2)
km_label = Label(text=f"is equal to  ___  km", fg="red", font=("Arial", 15))
km_label.grid(row=0, column=3)
calculate = Button(text="Calculate", command=calculate)
calculate.grid(row=2, column=1)

window.mainloop()


