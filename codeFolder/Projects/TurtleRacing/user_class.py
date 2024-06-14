from turtle import Turtle

STARTING_POSITION=(0,-280)
INCREMENT=15
BOUND_ONE=260
BOUND_TWO=280
HEADING=90

class User_Class(Turtle):
    def __init__(self):
        super().__init__()
        self.create_user()
    
    def create_user(self):
        self.setheading(HEADING)
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        new_y_pos=self.ycor()+INCREMENT
        if self.ycor()<BOUND_ONE:
            self.goto(x=self.xcor(),y=new_y_pos)
    
    def move_down(self):
        new_y_pos=self.ycor()-INCREMENT
        if self.ycor()>-BOUND_TWO:
            self.goto(x=self.xcor(),y=new_y_pos)
    
    def move_left(self):
        new_x_pos=self.xcor()-INCREMENT
        if self.xcor()>-BOUND_TWO:
            self.goto(x=new_x_pos,y=self.ycor())
    
    def move_right(self):
        new_x_pos=self.xcor()+INCREMENT
        if self.xcor()<BOUND_TWO:
            self.goto(x=new_x_pos,y=self.ycor())
    
