# https://docs.python.org/3/library/turtle.html#
# https://pypi.org/project/prettytable/ and https://github.com/jazzband/prettytable

from turtle import Turtle, Screen
import another_module
from prettytable import PrettyTable

print(another_module.another_variable)

timmy = Turtle()  # this is an object of the Turtle class
print(timmy)
timmy.shape("turtle")
timmy.color("DarkOliveGreen")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)