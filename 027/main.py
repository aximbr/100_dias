from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometer Converter")
#window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

#Labels
lbl_miles = Label(text="Miles")
lbl_miles.grid(column=2, row=0)
lbl_km = Label(text="Km")
lbl_km.grid(column=2, row=1)
lbl_equal = Label(text="is equal to ")
lbl_equal.grid(column=0, row=1)
lbl_result = Label(text=0)
lbl_result.grid(column=1, row=1)

#Entry
entry_miles = Entry(width=7)
entry_miles.grid(column=1, row=0)
entry_miles.focus()

#Button
def do_calculate():
    result = float(entry_miles.get()) * 1.609
    lbl_result.config(text=f"{result}")
    
bt_calculate = Button(text="Calculate", command=do_calculate)
bt_calculate.grid(column=1, row=2)

window.mainloop()