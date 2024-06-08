from turtle import Screen
from snake_class import Snake_Class
from food_class import Food
from track_score import Score
from outline_class import Outline
from welcome_class import Welcome
from difficulty_class import Difficulty
import time

FINALXPOS=270
FINALXNEG=-270
FINALYPOS=270
FINALYNEG=-270

sleep_duration=0.15

main_screen=Screen()
main_screen.listen()
main_screen.setup(width=600,height=600)
main_screen.bgcolor("black")
main_screen.tracer(0)

welcomeOne=Welcome()

def welcome():
    welcomeOne.display_welcome_message()
    welcomeOne.display_start_message()

def increase_difficulty():
    global sleep_duration
    sleep_duration-=0.005

def decrease_difficulty():
    global sleep_duration
    sleep_duration+=0.005

welcome()

def start_snake_game():

    global sleep_duration
    sleep_duration=0.15
    main_screen.resetscreen()
    welcome()
    welcomeOne.clear()
    game_is_on=True
    difficultyOne=Difficulty()
    snakeOne=Snake_Class()
    snakeOne.create_snakes()
    foodOne=Food()
    scoreOne=Score()
    outlineOne=Outline()

    main_screen.onkeypress(fun=snakeOne.move_snake_up,key="w")
    main_screen.onkeypress(fun=snakeOne.move_snake_back,key="s")
    main_screen.onkeypress(fun=snakeOne.move_snake_left,key="a")
    main_screen.onkeypress(fun=snakeOne.move_snake_right,key="d")
    main_screen.onkeypress(fun=increase_difficulty,key="plus")
    main_screen.onkeypress(fun=decrease_difficulty,key="minus")

    while game_is_on:
        main_screen.update()
        time.sleep(sleep_duration)
        snakeOne.move_snake()

        if snakeOne.snake_head.distance(foodOne) < 15:
            foodOne.refresh_location()
            scoreOne.increase_score()
            snakeOne.extend_snake()
        
        for snake_segments in snakeOne.snake_list[1:]:
            if snakeOne.snake_head.distance(snake_segments)<10:
                game_is_on=False
                scoreOne.game_over()
                scoreOne.restart_game()
        
        if snakeOne.snake_head.xcor()>FINALXPOS or snakeOne.snake_head.xcor()<FINALXNEG or snakeOne.snake_head.ycor()>FINALYPOS or snakeOne.snake_head.ycor()<FINALYNEG:
            game_is_on=False
            scoreOne.game_over()
            scoreOne.restart_game()
        
main_screen.onkeypress(fun=start_snake_game,key="space")
main_screen.exitonclick()
