from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE = "./data/french_words.csv"

current_card = {}
#-----------------pick random word ------------------#
def next_card():
    global current_card, delay
    window.after_cancel(delay)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text= current_card["French"], fill="black")
    delay = window.after(3000, flip_the_card)
    
def flip_the_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    global current_card
    canvas.itemconfig(card_title, text= "English",fill="white")
    canvas.itemconfig(card_word, text= current_card["English"], fill="white")
    

#-----------------main()-----------------------------#   
#-----------------Read csv file ---------------------#
data = pandas.read_csv(DATA_FILE)

#create a dictionary french-english
to_learn = data.to_dict(orient="records")



    
#-----------------User Interface---------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
delay = window.after(3000, flip_the_card)

card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
