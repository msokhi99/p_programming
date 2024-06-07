from turtle import Turtle, Screen, colormode
import random
from color_pallete import image_colors

colormode(255)

turtle_one = Turtle()
turtle_one.hideturtle()
turtle_one.penup()
turtle_one.shape("turtle")
turtle_one.speed("fastest")
turtle_one.setpos(-400, -300)

yPos = turtle_one.ycor()
for i in range(10):
    turtle_one.setpos(-400, yPos)
    yPos += 70
    for _ in range(10):
        turtle_one.penup()
        turtle_one.dot(20, random.choice(image_colors))
        turtle_one.forward(88)

turtle_one.home()
turtle_screen = Screen()
turtle_screen.exitonclick()
