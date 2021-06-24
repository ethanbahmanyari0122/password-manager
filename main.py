from tkinter import *
from tkinter import messagebox
import random
#to make a copy of the password in the clipboard
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_button_pressed():
    if len(website_entry.get()) == 0:
        messagebox.showinfo(message="Website field is empty!")
    elif len(password_entry.get()) == 0:
        messagebox.showinfo(message="Password field is empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: "
                                                                          f"\nEmail: {email_entry.get()}"
                                                                          f"\nPassword: {password_entry.get()}"
                                                                          f"\nIs it ok to save?")
        if is_ok:
            # https://www.w3schools.com/python/python_file_write.asp
            file_x = open("passwords.txt", "a")
            file_x.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            file_x.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(name="photo", file="ezgif.com-apng-to-gif.gif")
canvas.create_image(100, 100, image=logo_image)
# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
# Buttons
generate_button = Button(text="Generate Password", bg="Black", command=generate_pass)
add_button = Button(text="Add", width=36, command=add_button_pressed)
# entries
website_entry = Entry(width=35)
email_entry = Entry(width=35)
email_entry.insert(0, "ethan.bhm@outlook.com")
password_entry = Entry(width=17)
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
