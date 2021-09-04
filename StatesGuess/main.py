import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
map = pandas.read_csv("50_states.csv")
states = map["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correctly Guessed", prompt="What's the state name").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.ht()
        tim.penup()
        state_data = map[map["state"] == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)

missed_states = []
for check in states:
    if check not in guessed_states:
        missed_states.append(check)

missed_data = {
    'states': missed_states
}
missed_file = pandas.DataFrame(data=missed_data)
missed_file.to_csv("states_to_learn.csv")


turtle.mainloop()