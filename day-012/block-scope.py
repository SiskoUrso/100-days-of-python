# Block scope does not exist in Python

game_level = 3
enemies = ["skeleton", "zombie", "alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)