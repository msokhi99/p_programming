from turtle import Turtle

INCREMENT=1

class Level_Class(Turtle):
    def __init__(self):
        self.level=1
        super().__init__()
        self.create_level()
    
    def create_level(self):
        self.penup()
        self.goto(-240,260)
        self.hideturtle()
        self.color("black")
        self.write(arg=f"LEVEL: {self.level}",align="center",font=("Impact",14,"bold"))
    
    def increase_score(self):
        self.level+=INCREMENT
        self.clear()
        self.write(arg=f"LEVEL: {self.level}",align="center",font=("Impact",14,"bold"))
    
    def display_game_over(self):
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.color("black")
        self.write(arg=f"GAME OVER. You reached level {self.level}",align="center",font=("Impact",20,"bold"))