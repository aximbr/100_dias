import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

#read list of states
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

#start the game
is_game_run = True
score = 0
guesses_states = []

while len(guesses_states)< 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guesses_states)}/50 States Correct", prompt="What's another state name? ").title()
    #check the answer
    if answer_state == "Exit":
        #create a csv file with states that are missing
        missing_states = []
        for state in all_states:
            if state not in guesses_states:
                missing_states.append(state)
        
        pandas.DataFrame(missing_states).to_csv("missing_states.csv")
        break
    
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guesses_states.append(answer_state)
    

