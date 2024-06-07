from turtle import Turtle, Screen, colormode
import random

colormode(255)


def get_random_color():
    r1 = random.choice(range(1, 256))
    r2 = random.choice(range(1, 256))
    r3 = random.choice(range(1, 256))
    return (r1, r2, r3)


turtle_one = Turtle()
turtle_one.shape("turtle")
turtle_one.shapesize(1, 1)
turtle_one.color("grey")
turtle_one.pensize(3)
turtle_one.speed("fastest")

'''
Challenge 1:
'''


def make_square(turtle_obj):
    for _ in range(4):
        turtle_obj.forward(100)
        turtle_obj.left(90)


'''
Challenge 2:
'''


def make_dashed_line(turtle_obj):
    for _ in range(51):
        turtle_obj.pendown()
        turtle_obj.forward(5)
        turtle_obj.penup()
        turtle_obj.forward(5)


'''
Challenge 3:
'''


def various_shapes(turtle_obj):
    for i in range(3, 11):
        turtle_obj.color(get_random_color())
        degree_of_shape = 360 / i
        for j in range(0, i):
            turtle_obj.right(degree_of_shape)
            turtle_obj.forward(100)


'''
Challenge 4:
'''


def get_random_degree():
    return random.choice(range(0, 361))


def get_random_length():
    return random.choice(range(0, 31))


def random_walk(turtle_obj):
    turtle_movement = [
        turtle_obj.forward,
        turtle_obj.backward,
        turtle_obj.left,
        turtle_obj.right
    ]
    for _ in range(1001):
        turtle_obj.color(get_random_color())
        move_turtle = random.choice(turtle_movement)
        if move_turtle in [turtle_obj.left, turtle_obj.right]:
            move_turtle(get_random_degree())
        else:
            move_turtle(get_random_length())


'''
Challenge 5:
'''


def spirograph(turtle_obj):
    turn_radius = 2
    for _ in range(int(360 / turn_radius)):
        turtle_obj.color(get_random_color())
        turtle_obj.circle(100)
        turtle_obj.left(turn_radius)


# make_square(turtle_one)
# make_dashed_line(turtle_one)
# various_shapes(turtle_one)
# random_walk(turtle_one)
spirograph(turtle_one)
turtle_screen = Screen()
turtle_screen.exitonclick()
