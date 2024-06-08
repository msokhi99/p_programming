from turtle import Turtle

class Outline(Turtle):
    def __init__(self):
        super().__init__()
        self.make_outline()
    
    def make_outline(self):
        self.color("red")
        self.ht()
        self.penup()
        self.goto(-270,-270)
        self.pendown()
        self.goto(270,-270)
        self.goto(270,270)
        self.goto(-270,270)
        self.goto(-270,-270)
