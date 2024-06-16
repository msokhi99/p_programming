from turtle import Turtle

class Map_Marker(Turtle):
    def __init__(self,x,y,state_name):
        super().__init__()
        self.create_marker(x=x,y=y,state_name=state_name)
    
    def create_marker(self,x,y,state_name):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=x,y=y)
        self.write(arg=state_name,font=("Arial",8,"bold"))