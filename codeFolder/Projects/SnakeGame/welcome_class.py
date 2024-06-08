from turtle import Turtle

WELCOMETEXT="WELCOME TO SNAKE"
STARTTEXT="PRESS SPACE TO START"
ALIGN="center"
FONT=('Courier',12,'bold')

class Welcome(Turtle):
    def __init__(self):
        super().__init__()
        self.display_welcome_message()
    
    def display_welcome_message(self):
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.hideturtle()
        self.write(arg=f"{WELCOMETEXT}",align=ALIGN,font=FONT)
    
    def display_start_message(self):
        self.penup()
        self.color("white")
        self.goto(0,-20)
        self.hideturtle()
        self.write(arg=f"{STARTTEXT}",align=ALIGN,font=FONT)