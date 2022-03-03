import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




condition = True 
while condition == True:
    answer_state = screen.textinput(title="Guess the state", prompt="Whats another state's name?").title()
    for statees in data.state:
        if statees == answer_state:
            test = data[data.state == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(test.x),int(test.y))
            t.write(answer_state)
            print(test.x)



screen.exitonclick()