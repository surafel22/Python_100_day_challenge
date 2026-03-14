from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website:
                    {
                    "email": email,
                    "password": password
                    }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please enter all fields")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These the details entered:\n "
                                                      f"Email: {email}\nPassword: {password}\n "
                                                              f"Is this ok to save")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

#--------------------------search----------------#

def search():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)


    except FileNotFoundError:
        messagebox.showerror("Error", "No such data exists")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror("Error", f"No such {website} website exists")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white")
canvas.grid(row=0, column=1)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)

web_label = Label(text = "Website:")
web_label.grid(row=1, column=0)
email_label = Label(text = "Email:")
email_label.grid(row=2, column=0)
pass_label = Label(text = "Password:")
pass_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
email_entry = Entry(width=35)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sura@gmail.com")

pass_entry = Entry(width=35)
pass_entry.grid(row=3, column=1,columnspan=2)

generate_password_button = Button(text = "Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text = "Add",width = 36, command = save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text = "Search",command=search )
search_button.grid(row=1, column=2, columnspan=2)

window.mainloop()
