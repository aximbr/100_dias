from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0,9)

@app.route("/")
def hello():
    return '<h1> Guess a number between 0 and 9</h1>\
        <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'
        
@app.route("/<int:guess>")
def check_number(guess):
    global number
    if guess < number:
        return "<h1 style='color: purple'> Too low, try again </h1>\
            <img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"    
    elif guess > number:
        return "<h1style='color: red'> Too high, try again </h1>\
            <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    else:
        return "<h1 style='color: green'> You Found me!</h1>\
            <img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"

#main()

if __name__ == "__main__":
    app.run(debug=True)