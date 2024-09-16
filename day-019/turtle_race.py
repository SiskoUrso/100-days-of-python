from turtle import Screen, Turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your Bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've Lost! The winning turtle was the {winner_color} turtle.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()