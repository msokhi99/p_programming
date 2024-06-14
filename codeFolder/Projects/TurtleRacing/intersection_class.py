from turtle import Turtle

COORDS=[(290,-240),(290,-200),(290,-160),(290,-120),(290,-80),(290,-40),(290,0),(290,40),(290,80),    (290,120),(290,160),(290,200),(290,240)]

X_COORD_CUT_OFF=300
INCREMENT=10
HEADING=180

class Intersection_Lines(Turtle):
    def __init__(self):
        super().__init__()
        self.create_intersection()
    
    def create_intersection(self):
        for positions in COORDS:
            self.hideturtle()
            self.penup()
            self.color("black")
            self.shape("arrow")
            self.goto(positions)
            self.setheading(HEADING)
            while self.xcor()>-X_COORD_CUT_OFF:
                self.pendown()
                self.forward(INCREMENT)
                self.penup()
                self.forward(INCREMENT)
