import turtle as t
from random import choice, randint

tim = t.Turtle()
tim.shape("turtle")
tim.color("springgreen3")
#tim.pensize(15)
tim.speed(0)
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

# 360 / sides of shape to determine angle
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# for shape_side_n in range(3, 11):
#     tim.color(random_color())
#     draw_shape(shape_side_n)

# square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# random walk
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(choice([0, 90, 180, 270]))

# spirograph
draw_spirograph(5)




screen = t.Screen()
screen.exitonclick()
