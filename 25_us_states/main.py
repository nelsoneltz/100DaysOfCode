import pandas as pd
import turtle


screen = turtle.Screen()
screen.title("US States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name?")
    if answer_state != None:
        answer_state = answer_state.title()
    if answer_state == None or answer_state == 'Exit':
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto((int(state_data.x),int(state_data.y)))
        t.write(answer_state) # t.write(state_data.state.item()) 

missing_states = [state for state in all_states if state not in guessed_states ]
save_df = pd.DataFrame(missing_states)
save_df.to_csv('missing_states.csv')

screen.exitonclick()
