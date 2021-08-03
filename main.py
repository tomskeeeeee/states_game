import turtle
import pandas


# set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")
# use the blank map image as the background of the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
state_text = turtle.Turtle()
state_text.penup()
state_text.hideturtle()
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.color("blue")

# get data from file
states_data = pandas.read_csv("50_states.csv")
list_of_states = states_data["state"].to_list()
# print(list_of_states)
# convert given state names to all lowercase to match regardless of case
# list_of_states = list(pandas.Series(list_of_states).str.lower())

list_of_states = [state.lower() for state in list_of_states]

def print_missed_states(list_of_misses):
    state_text.color("red")
    for guess in list_of_misses:
        state_row = states_data[states_data.state.str.lower() == guess]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        state_text.goto(x_cor, y_cor)
        state_text.write(guess)



num_states_correct = 0
num_guesses = 0
guessed_states = []
is_done = False
while num_states_correct < 50 and num_guesses < 100 and not is_done:

    guess = screen.textinput(title=f"You have {num_states_correct}/50 correct", prompt="Type a state: ").lower()
    if guess == "q":
        is_done = True

    num_guesses += 1
    # check if state is in list

    if guess in list_of_states:
        num_states_correct += 1
        guessed_states.append(guess)
        # get x,y location of state
        state_row = states_data[states_data.state.str.lower() == guess]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        state_text.goto(x_cor, y_cor)
        state_text.write(guess)

game_over.setposition(0, 240)
missed_states = [state for state in list_of_states if state not in guessed_states]
print_missed_states(missed_states)
game_over.write(f"You used {num_guesses} guesses to get {len(guessed_states)} correct", align="center", font=("Courier", 18))
turtle.mainloop()

# add name to correct x, y location on map

# this code was used to figure out location of each state on teh ap
# def get_mouse_click_coord(x, y):
#     print(x, y)
# # event listener for mouse clicks on the screen(map)
# turtle.onscreenclick(get_mouse_click_coord)
# # keep screen open even while clicking
# turtle.mainloop()

