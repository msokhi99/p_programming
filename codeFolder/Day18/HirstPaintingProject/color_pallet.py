import colorgram

colors = colorgram.extract('spot.jpg', 30)
image_colors = []

for i in range(len(colors)):
    r1 = colors[i].rgb[0]
    r2 = colors[i].rgb[1]
    r3 = colors[i].rgb[2]
    tempTuple = (r1, r2, r3)
    image_colors.append(tempTuple)
