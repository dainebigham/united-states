import turtle as t
import pandas as pd

data = pd.read_csv('50_states.csv')
states = data.state.to_list()

screen = t.Screen()
screen.title('United Stated Quiz')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

state = t.Turtle()
state.pu()
state.hideturtle()

states_guessed = []

while len(states_guessed) < 50:
    answer = screen.textinput(title=f'{len(states_guessed)}/50 States Correct', prompt='Enter State: ').title()

    if answer in states:
        new_state = data[data.state == answer]
        state_xy = (int(new_state.x), int(new_state.y))

        state.goto(state_xy)
        state.write(new_state.state.item())

        states_guessed.append(answer)
    if answer == 'Exit':
        states_missed = []

        for state in states: 
            if state not in states_guessed:
                states_missed.append(state)

        states_missed_csv = pd.DataFrame(states_missed)
        states_missed_csv.to_csv('States_to_learn.csv')

        break