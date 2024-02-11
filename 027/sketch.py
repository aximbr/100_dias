#Day 027 - personal notes and exercices
from tkinter import *


window = Tk()
window.title("This is my first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a Label!", font =("Arial", 24, "bold"))
my_label.config(text="Ultimo texto")
my_label.grid(column=0,row=0)
  
# Entry box
my_entry = Entry()
my_entry.grid(column=3, row=2)

# Button
def button_clicked():
    my_label["text"] = my_entry.get()
    
my_button = Button(text="This is a button", command=button_clicked)
my_button.grid(column=1, row=1)

my_new_button = Button(text="New Button" )
my_new_button.grid(column=3, row=0)






window.mainloop()

