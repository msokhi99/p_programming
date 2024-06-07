import turtle
from turtle import Turtle,Screen
import random

color_pallet=["red","blue","green","black","yellow"]
turtle_players=[]
def make_turtle_obj():
    for i in range(5):
        turtle_obj=Turtle("turtle")
        turtle_obj.color(color_pallet[i])
        turtle_obj.speed("fastest")
        turtle_obj.penup()
        turtle_players.append(turtle_obj)
def turtle_initial_pos():
    y_pos=-200
    for i in range(5):
        turtle_players[i].goto(-630,y_pos)
        y_pos+=100

def get_random_length():
    temp_random=random.randint(0,10)
    return temp_random
def make_turtle_move_randomly():
    game_running = True
    while game_running:
        for turtles in turtle_players:
            if turtles.xcor() < 610:
                turtles.forward(get_random_length())
            elif turtles.xcor() >= 610:
                winner=turtles
                game_running=False
                return winner
def get_user_choice():
    temp_choice=turtle.textinput(title="Make a Bet",prompt="Please choose a color:"
                                "\nRed, Blue, Green, Black, Yellow").lower()
    while temp_choice not in color_pallet:
        temp_choice = turtle.textinput(title="Make a Bet", prompt=f"{temp_choice} is not in the pallet. "
                                      f"Please choose a color: \nRed, Blue, Green, Black, Yellow").lower()
    return temp_choice

def check_bet(user_winner,actual_winner):
    if user_winner==actual_winner.pencolor():
        print("Congratulations. You won.")
    else:
        print(f"You lost. The winner was the {actual_winner.pencolor()} turtle.")

def restart_game(screen_obj):
    temp_restart=turtle.textinput(title="Restart Game",prompt="Enter (Y) to restart or (Q) to quit.").lower()
    if temp_restart=="y":
        turtle_race()
    else:
        screen_obj.bye()

first_game=True
def turtle_race():
    global first_game
    user_choice=get_user_choice()
    if user_choice:
        if first_game:
            make_turtle_obj()
            first_game=False
        turtle_initial_pos()
        get_winner=make_turtle_move_randomly()
        check_bet(user_winner=user_choice,actual_winner=get_winner)

    turtle_screen=Screen()
    turtle_screen.title("Turtle Race")
    restart_game(turtle_screen)

turtle_race()
