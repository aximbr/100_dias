from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

WHITE = "#ffffff"
FILENAME = "data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    entry_password.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #using List comprehension
    password_list = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #using List comprehension
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    #using List comprehension
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)

    #using join to converter from list to a string
    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email" : username,
            "password": password
            }
        }
    
        
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title= "Error", message="Please don't leave any field empty!")
    else:       
        try:
            with open(FILENAME, "r") as data_file:
                #reading the old file
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open(FILENAME, "w") as data_file:
                #create a new file
                json.dump(new_data, data_file, indent=4)
            
        else:
            #update with new data
            data.update(new_data)
            with open(FILENAME, "w") as data_file:
                #saving update data on file
                json.dump(data, data_file, indent=4)
                
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()
#----------------------------- SEARCH -------------------------------- #
def find_password():
    website = entry_website.get()
    username = ""
    password = ""
        
    if len(website) == 0:
        messagebox.showerror(title= "Error", message="Please don't leave any field empty!")
    else:       
        try:
            with open(FILENAME, "r") as data_file:
                #reading the data file
                data = json.load(data_file)
                
        except FileNotFoundError:
            messagebox.showerror(title= "Error", message="No Datafile found!")
              
        else:
            #search for website
            # try:
            #     username = data[website]['email']
            #     password = data[website]['password']
            # except KeyError:
            #     messagebox.showerror(title= website, message=f"No details for {website} exists.")
            # else:
            #     messagebox.showinfo(title= website, message=f"username: {username}\npassword: {password}")
            if website in data:
                username = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title= website, message=f"username: {username}\npassword: {password}") 
            else:
                messagebox.showinfo(title= website, message=f"No details for {website} exists.")  
        
        entry_website.focus()        
    
     

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

entry_website = Entry(width=30, highlightthickness=1)
entry_website.grid(column=1, row=1, columnspan=2, sticky="W", pady=2)
entry_website.focus()

entry_username = Entry(width=30, highlightthickness=1)
entry_username.grid(column=1, row=2, columnspan=2, sticky="W", pady=2)
entry_username.insert(0, "jose.p.leitao@gmail.com")

entry_password = Entry(width=30, highlightthickness=1)
entry_password.grid(column=1, row=3, sticky="W", pady=2)

button_generate = Button(text="Generate Password", command=gen_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save_to_file)
button_add.grid(column=1, row=4, columnspan=2, sticky="W")

button_search = Button(text="Search", command=find_password)
button_search.grid(column=2, row=1, sticky="W")

window.mainloop()