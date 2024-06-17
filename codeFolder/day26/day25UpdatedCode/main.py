from turtle import Screen,Turtle
import pandas as pd
from map_marker import Map_Marker

# Constants:
FILE_NAME="./50_states.csv"
SCREEN_WIDTH=700
SCREEN_HEIGHT=490
SCREEN_BG_COLOR="black"
SCREEN_BG_PIC="blank_states_img.gif"
TOTAL_US_STATES=50

# DataFrame Setup:
game_df=pd.read_csv(FILE_NAME)
# print(game_df.head())
us_states=game_df["state"].to_list()

# Screen Setup
main_screen=Screen()
main_screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
main_screen.bgcolor(SCREEN_BG_COLOR)
main_screen.title(titlestring="U.S. State Guessing Game")
main_screen.bgpic(picname=SCREEN_BG_PIC)

# Misc:
total_states=TOTAL_US_STATES
correct_guesses=0
user_answers=[]
game_is_on=True

# Logic:
while game_is_on:
    if correct_guesses==50:
        print("You have guessed all the states.")
        game_is_on=False
    user_input=main_screen.textinput(title=f"{correct_guesses}/{total_states} states guessed correctly.",prompt="Guess a state:").title()
    if user_input=="Exit":
        game_is_on=False
        # CSV Output (Updated List Comprehension)
        states_missed=[states for states in us_states if states not in user_answers]
        output_data=pd.DataFrame(data=states_missed)
        output_data.to_csv("./Output.csv")
    if user_input in us_states and user_input not in user_answers:
        user_answers.append(user_input)
        correct_guesses+=1
        user_input_data=game_df[game_df["state"]==user_input]
        user_input_data_x_cord=user_input_data["x"].iloc[0]
        user_input_data_y_cord=user_input_data["y"].iloc[0]
        map_location_marker=Map_Marker(x=user_input_data_x_cord,y=user_input_data_y_cord,state_name=user_input)
    elif user_input in user_answers:
        print("Repetitive Guess.")
    elif user_input not in us_states:
        if user_input!="Exit":
            print("Non-existent state.")

# Test Code:
# main_screen.listen()
# test_point=Turtle()
# test_point.penup()
# test_point.color("red")
# test_point.shape("circle")
# test_point.goto(x=-297,y=13)

# def get_coords(x,y):
#     print(x,y)

# main_screen.onscreenclick(fun=get_coords)

# # CSV Output:
# states_missed=[]
# for states in us_states:
#     if states not in user_answers:
#         states_missed.append(states)

# output_data=pd.DataFrame(data=states_missed)
# output_data.to_csv("./Output.csv")
