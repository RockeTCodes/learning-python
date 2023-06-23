import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S Staes Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = list(data.state)
guessed_states = []


while len(guessed_states) < 50:
    user_answer = (screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="Input your geuss here")).title()
    if user_answer == "Exit":
        not_guessed_states = []
        [not_guessed_states.append(state)
         for state in states if state not in guessed_states]
        dict = {"States": not_guessed_states}
        data_frame = pandas.DataFrame(dict)
        data_frame.to_csv("left_states.csv")

        break
    if user_answer in states:
        xcor = (data[data.state == user_answer].x).iloc[0]
        ycor = (data[data.state == user_answer].y).iloc[0]
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(xcor, ycor)
        new_state.write(user_answer)
        guessed_states.append(user_answer)

turtle.mainloop()
