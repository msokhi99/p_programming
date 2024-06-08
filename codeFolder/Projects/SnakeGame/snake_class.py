from turtle import Turtle

YPOS=0
STEPS=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
INITIALCOORDS=[(0,0)]

class Snake_Class:
    def __init__(self):
        self.snake_list=[]
        self.create_snakes()
        self.snake_head=self.snake_list[0]
        self.snake_head.color("blue")
    
    def create_snakes(self):
       self.update_snake(INITIALCOORDS[0])
    
    def update_snake(self,coords):
        snake_obj=Turtle()
        snake_obj.penup()
        snake_obj.shape("square")
        snake_obj.color("white")
        snake_obj.goto(coords)
        self.snake_list.append(snake_obj)
    
    def extend_snake(self):
        self.update_snake(self.snake_list[-1].position())
    
    def move_snake(self):
        for i in range(len(self.snake_list)-1,0,-1):
            self.snake_list[i].goto(self.snake_list[i-1].xcor(),self.snake_list[i-1].ycor())
        self.snake_head.forward(STEPS)
    
    def move_snake_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)
    
    def move_snake_back(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)
    
    def move_snake_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)
    
    def move_snake_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)
            