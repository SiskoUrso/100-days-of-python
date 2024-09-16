from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.color("white")

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.reset()

screen.bgcolor("black")
screen.title("Etch-A-Sketch")
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()