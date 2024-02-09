from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(height=250, width=300, bg="white")
        false_image = PhotoImage(file="./images/false.png")
        true_image = PhotoImage(file="./images/true.png")
        self.q_text = self.canvas.create_text(150,
                                              125,
                                              text="Some text",
                                              fill=THEME_COLOR,
                                              font=("Ariel",20,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.false_button = Button(image=false_image, highlightthickness=0, command=None)
        self.false_button.grid(column=1, row=2)
        
        self.true_button = Button(image=true_image, highlightthickness=0, command=None)
        self.true_button.grid(column=0, row=2)
        
        self.score_lbl = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel",12))
        self.score_lbl.grid(row=0, column=1)

        
        self.window.mainloop()

