import requests
from datetime import datetime
import os

USER_WEIGHT=80
USER_HEIGHT=182.88
USER_AGE=24

user_query=str(input("Tell me what did you do for your workout: "))

current_day_details=datetime.today()

def get_current_date():
    current_date=current_day_details.date().strftime("%d/%m/%Y")
    return current_date

def get_current_time():
    current_time=current_day_details.time().strftime("%H:%M:%S")
    return current_time

APP_ID=os.environ.get("APPID")
API_KEY=os.environ.get("APIKEY")

header_for_nutrition_api={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

payload_for_nutrition_api={
    "query":user_query,
    "weight_kg":USER_WEIGHT,
    "height_cm":USER_HEIGHT,
    "age":USER_AGE,
}

nutrition_api_request=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=payload_for_nutrition_api
                          ,headers=header_for_nutrition_api)
data_received_from_api=nutrition_api_request.json()

def get_exercise_from_data():
    exercise_done=data_received_from_api["exercises"][0]["name"]
    return exercise_done.title()

def get_calories_burned_from_data():
    calories_burned=data_received_from_api["exercises"][0]["nf_calories"]
    return calories_burned

def get_duration_from_data():
    duration=data_received_from_api["exercises"][0]["duration_min"]
    return duration

payload_for_sheet_api={
    "workout":{
        "date":get_current_date(),
        "time":get_current_time(),
        "exercise":get_exercise_from_data(),
        "duration":get_duration_from_data(),
        "calories":get_calories_burned_from_data(),
    }
}

header_for_sheet_api={"Authorization":"Bearer giveaccesstotheownerofthisspreadsheet"}

def add_row_in_sheet():
    requests.post(url="https://api.sheety.co/44887629ed4facd9ea23b932e49c0e96/workoutTracking/workouts",json=payload_for_sheet_api
                        ,headers=header_for_sheet_api)

program_running=True

add_row_in_sheet()
