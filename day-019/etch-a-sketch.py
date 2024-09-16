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
    tim.shape("classic")
    tim.color("white")
    
def change_shape():
    user_choice = screen.textinput(title="Choose a shape between 'arrow', 'turtle', 'circle', 'square', 'triangle'", prompt="Pick a shape: ")
    tim.shape(user_choice)
    screen.listen()
    
def stamp():
    tim.stamp()
    
def change_background_color():
    user_choice = screen.textinput(title="Choose a background color", prompt="Pick a color: ")
    screen.bgcolor(user_choice)
    screen.listen()
    
def change_color():
    user_choice = screen.textinput(title="Choose a pen color", prompt="Pick a color: ")
    tim.color(user_choice)
    screen.listen()
    
def pen_size():
    user_choice = screen.textinput(title="Pen Size", prompt="Choose a number from 1 - 10: ")
    tim.pensize(int(user_choice))
    tim.resizemode("auto")
    screen.listen()
    
def pen_up():
    tim.penup()
    
def pen_down():
    tim.pendown()
    
def change_color_red():
    tim.color("red")
    
def change_color_green():
    tim.color("green")
    
def change_color_blue():
    tim.color("blue")
    

screen.bgcolor("black")
screen.title("Etch-A-Sketch")
screen.listen()
screen.onkey(change_background_color, "u")
screen.onkey(change_color, "t")
screen.onkey(change_shape, "i")
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.onkey(change_color_red, "r")
screen.onkey(change_color_green, "g")
screen.onkey(change_color_blue, "b")
screen.onkey(pen_up, "q")
screen.onkey(pen_down, "e")
screen.onkey(pen_size, "p")
screen.onkey(stamp, "space")


screen.exitonclick()