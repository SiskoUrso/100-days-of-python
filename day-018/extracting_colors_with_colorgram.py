import colorgram  # https://pypi.org/project/colorgram.py/

colors = colorgram.extract("image.jpg", 25)

color_pallet = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_pallet.append(new_color)
    
print(color_pallet)