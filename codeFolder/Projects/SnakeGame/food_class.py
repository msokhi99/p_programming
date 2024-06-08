from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.refresh_location()
    
    def refresh_location(self):
        random_x_pos=random.randint(-255,255)
        random_y_pos=random.randint(-255,255)
        self.goto(x=random_x_pos,y=random_y_pos)