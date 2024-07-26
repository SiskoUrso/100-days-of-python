states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"] # this is a list which uses square brackets, the ordering of the list is important

print(states_of_america[4]) # inside the bracktes is the index or the offset or the position of the item in the list (0 = 1st item, 1 = 2nd item, etc.) *can use negative index to start counting from the end of the list (ex. -1 = last item, -2 = 2nd last item, etc.)

states_of_america[1] = "Pencilvania" # can change the item in the list by using the index and assigning it a new value

states_of_america.append("Angelaland") # can add an item to the end of the list using the append function

states_of_america.extend(["Angelaland", "Jack Bauer Land"]) # can add multiple items to the end of the list using the extend function

num_of_states = len(states_of_america) # can use the len function to get the number of the list items

print(states_of_america[num_of_states - 1]) # here we are using the len function to get the number of the list items and then subtracting 1 to get the last item in the list.

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # this is a nested list, a list that contains multiple lists , nested lists are accessed using the index of the outer list and then the index of the inner list which is also considered left to right

print(dirty_dozen[1][1]) # this will print the 2nd item in the 2nd list, which is Kale