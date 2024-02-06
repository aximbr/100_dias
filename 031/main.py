from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"

#-----------------User Interface---------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Ariel",40,"italic"))
canvas.create_text(400, 263, text="word", font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=None)
unknown_button.grid(column=0, row=1)
right_button = Button(image=right_image, highlightthickness=0, command=None)
right_button.grid(column=1, row=1)

window.mainloop()
