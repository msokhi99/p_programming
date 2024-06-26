import requests
import datetime as dt 
import weather_codes as codes
import smtplib as sm
import os

sender_email=os.environ.get("SENDEREMAIL")
sender_pass=os.environ.get("PASS")
reciever="bobbysokhi1@gmail.com"

w_code=codes.weather_code

current_time=dt.datetime.now().isoformat()

params={
    "location":"49.104599 -122.823509",
    "fields":["weatherCode"],
    "units":"metric",
    "timesteps":["1h"],
    "startTime":current_time,
    "endTime":"nowPlus1h",
    "apikey":"USE OWN KEY"
}

response=requests.get(url="https://api.tomorrow.io/v4/timelines",params=params)
response.raise_for_status()
data=response.json()
new_data={}
timelines = data['data']['timelines']
for timeline in timelines:
    intervals = timeline['intervals']
    for interval in intervals:
        start_time = interval['startTime']
        weather_code = interval['values']['weatherCode']
        new_data[start_time] = str(weather_code)

message_to_send="Weather data for the next couple hours:\n\n"
weather_data=[]

for start_time, weather_code in new_data.items():
    description = w_code[weather_code]
    weather_data.append(f"At {start_time} : {description}")

message_to_send+="\n".join(weather_data)

with sm.SMTP("smtp.gmail.com",port=587) as new_connection:
    new_connection.starttls()
    new_connection.login(user=sender_email,password=sender_pass)
    new_connection.sendmail(from_addr=sender_email,to_addrs=reciever,msg=f"Subject: Daily Weather Report: \n\n{message_to_send}")
