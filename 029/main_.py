from tkinter import *
WHITE = "#ffffff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)




canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

lbl_website = Label(text="Website:", bg=WHITE)
lbl_website.grid(column=0, row=1, sticky="E")

lbl_user_name = Label(text="Email/Username:", bg=WHITE)
lbl_user_name.grid(column=0, row=2)

lbl_password = Label(text="Password:", bg=WHITE)
lbl_password.grid(column=0, row=3, sticky="E")

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2, sticky="W")

entry_username = Entry(width=35)
entry_username.grid(column=1, row=2, columnspan=2, sticky="W")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, sticky="W")

button_generate = Button(text="Generate Password", command=None)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=None)
button_add.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()