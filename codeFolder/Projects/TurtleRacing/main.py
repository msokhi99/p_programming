from turtle import Screen
from user_class import User_Class
from intersection_class import Intersection_Lines
from car_class import Car_Class
from level_class import Level_Class
import time

DISTANCE=22
PONE_YCOR=260
PONE_GOTO=280
SCREEN_WIDTH=600
SCREEN_HEIGHT=600

# Main Screen Setup:
main_screen=Screen()
main_screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
main_screen.bgpic(picname="new_squirtle.gif")
main_screen.title(titlestring="Turtle Crossing Game")
main_screen.tracer(0)
main_screen.listen()

# Objects on Screen:
player_one=User_Class()
lane_intersection=Intersection_Lines()
new_car=Car_Class()
levels=Level_Class()

# Main Controls:
main_screen.onkeypress(fun=player_one.move_up,key="w")
main_screen.onkeypress(fun=player_one.move_down,key="s")
main_screen.onkeypress(fun=player_one.move_left,key="a")
main_screen.onkeypress(fun=player_one.move_right,key="d")

# Game Logic: 
def main():
    game_is_running=True
    while game_is_running:
        main_screen.update()
        time.sleep(0.1)
        new_car.create_car()
        new_car.move_car()
        if player_one.ycor()==PONE_YCOR:
            levels.increase_score()
            player_one.goto(0,-PONE_GOTO)
            new_car.increase_increment()
        for cars in new_car.all_cars:
            if player_one.distance(cars)<DISTANCE:
                game_is_running=False
                levels.display_game_over()

main()
main_screen.exitonclick()
