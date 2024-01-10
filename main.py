from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    formatted_data = f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n"
    with open("data.txt", "a") as file:
        file.write(formatted_data)
    print(formatted_data)
    reset_entries()

def reset_entries():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, "jcalinquant@hotmail.com")
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Row 0
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Row 1
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Row 2
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "jcalinquant@hotmail.com")

# Row 3
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
generate_pwd_btn = Button(text="Generate Password")
generate_pwd_btn.grid(row=3, column=2)

# Row 4
add_btn = Button(text="Add", width=36, command=add_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
