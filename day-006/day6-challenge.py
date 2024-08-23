#The challenge was to use a site called reeborg (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) where you controlled
#a robot to solve a maze. The goal was to use if and while loops. The code by itself will no function but if you enter this code into the link above it will solve every soltuion.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
    
while not at_goal():    
    if right_is_clear() and wall_on_right:
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()