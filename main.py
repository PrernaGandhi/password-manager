import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    # delete any data written previously
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

    # to copy the password
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    # save data to file
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    formatted_text = f"{website} | {email} | {password}\n"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Ooops!", message="Please don't leave any fields empty !")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(formatted_text)
            # clear website and password entries
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            # refocus to website entry
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, )
logo = tkinter.PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_label = tkinter.Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = tkinter.Entry(width=38)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "dummy@gmail.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
