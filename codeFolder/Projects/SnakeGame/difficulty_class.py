from turtle import Turtle

TEXTINCREASE="""Increase difficulty: \nPress +"""
ALIGN="center"
FONT=('Courier',8,'bold')

TEXTDECREASE="""Decrease difficulty: \nPress -"""
ALIGN="center"
FONT=('Courier',8,'bold')

class Difficulty(Turtle):
    def __init__(self):
        super().__init__()
        self.display_increase()
        self.display_decrease()
    
    def display_increase(self):
        self.penup()
        self.color("white")
        self.goto(-195,270)
        self.hideturtle()
        self.write(arg=f"{TEXTINCREASE}",align=ALIGN,font=FONT)
    
    def display_decrease(self):
        self.penup()
        self.color("white")
        self.goto(205,270)
        self.hideturtle()
        self.write(arg=f"{TEXTDECREASE}",align=ALIGN,font=FONT)