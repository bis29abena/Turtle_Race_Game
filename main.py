import turtle
import random
screen = turtle.Screen()

#Setting up the window for the turtle race
#With width 500 and height 400
screen.setup(width=500, height=300)
is_race_on = False
#Creating a prompt window for the turtle game
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race: enter color? ")
#Creating the colors for our turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_turtles = []

y_position = -100
#Creating 6 turtles using a for loop
for color in colors:
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 35
    list_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle_ in list_turtles:

        if turtle_.xcor() > 230:
            winning_turtle = turtle_.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f"You've won the {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost the {winning_turtle} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle_.forward(rand_distance)

screen.exitonclick()
