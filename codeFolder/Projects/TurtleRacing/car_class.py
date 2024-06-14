from turtle import Turtle,colormode
import random

colormode(255)
COORDS=[(290,-220),(290,-180),(290,-140),(290,-100),(290,-60),(290,-20),(290,20),(290,60),(290,    100),   (290,140),(290,180),(290,220)]
HEADING=180
INCREMENT=3
LENGTH=1.3
WIDTH=0.8

def random_color():
    r1=random.randint(0,255)
    r2=random.randint(0,255)
    r3=random.randint(0,255)
    return r1,r2,r3

class Car_Class():
    def __init__(self):
        self.all_cars=[]
        self.increment=INCREMENT
    
    def check_if_location_is_occupied(self,car_position):
        for cars in self.all_cars:
            if cars.position==car_position:
                return True
        return False
    
    def create_car(self):
        random_chance=random.randint(1,5)
        if random_chance==1:
            car_obj=Turtle()
            car_obj.penup()
            car_obj.shape("square")
            car_obj.color(random_color())
            car_obj.shapesize(stretch_len=LENGTH,stretch_wid=WIDTH)
            car_obj.setheading(HEADING)
            while True:
                random_location=random.choice(COORDS)
                if self.check_if_location_is_occupied(random_location)==False:
                    car_obj.goto(random_location)
                    self.all_cars.append(car_obj)
                    break
    
    def move_car(self):
        for cars in self.all_cars:
            cars.forward(self.increment)
    
    def increase_increment(self):
        self.increment+=INCREMENT
