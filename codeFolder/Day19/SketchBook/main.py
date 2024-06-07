import turtle
from turtle import Turtle,Screen

turtle_one=Turtle()
turtle_one.shape("turtle")
turtle_one.color("red")
turtle_one.pensize(2)
turtle_one.speed("fastest")
turtle.listen()

def move_forward():
    turtle_one.forward(3)
def move_backward():
    turtle_one.backward(3)
def move_clockwise():
    turtle_one.right(3)
def move_counter_clockwise():
    turtle_one.left(3)
def clear_screen():
    turtle_one.clear()
    turtle_one.penup()
    turtle_one.home()
    turtle_one.pendown()

turtle.onkeypress(fun=move_forward, key="w")
turtle.onkeypress(fun=move_backward, key="s")
turtle.onkeypress(fun=move_clockwise, key="d")
turtle.onkeypress(fun=move_counter_clockwise, key="a")
turtle.onkeypress(fun=clear_screen, key="c")

turtle_screen=Screen()
turtle_screen.exitonclick()
