import requests
import datetime as date
import smtplib as sm

'''API PATH'S'''

ISS_PATH="http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_PATH="https://api.sunrise-sunset.org/json"

'''CONSTANTS'''
MY_LAT=49.104599
MY_LNG=-122.823509

'''SUNRISE API PARAMS'''
sunrise_params={"lat":MY_LAT,"lng":MY_LNG,"formatted":0}

'''OPEN API'S'''

iss_api_response=requests.get(url=ISS_PATH)
iss_api_response.raise_for_status()
sunrise_sunset_api_response=requests.get(url=SUNRISE_SUNSET_PATH,params=sunrise_params)

'''GET DATA FROM API'S'''
iss_data=iss_api_response.json()
iss_latitude=float(iss_data["iss_position"]["latitude"])
iss_longitude=float(iss_data["iss_position"]["longitude"])

sunrise_data=sunrise_sunset_api_response.json()
sunrise_time=int(sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_time=int(sunrise_data["results"]["sunset"].split("T")[1].split(":")[0])

'''USER CURRENT TIME'''
user_current_time=date.datetime.now()
user_current_hour=user_current_time.hour

'''SENDER INFO'''
sender_email="sokhimantej99@gmail.com"
sender_pass="Random Password"

'''RECEIPIENT INFO'''
receiver_email="bobbysokhi1@gmail.com"

'''LOGIC'''
if 44 <= iss_latitude <= 54 and -127 <= iss_longitude <= -117:
    if sunset_time <= user_current_hour <= sunrise_time:
        with sm.SMTP("smtp.gmail.com",port=587) as new_connection:
            new_connection.starttls()
        try:
            new_connection.login(user=sender_email,password=sender_pass)
        except sm.SMTPAuthenticationError as error_message:
            print(f"Error {error_message}")
        else:
            try:
                new_connection.sendmail(from_addr=sender_email,to_addrs=receiver_email,msg="Subject:ISS SIGHTING\n\nThe ISS is approacing you. Please look up at the sky.")
            except sm.SMTPException as error_message:
                print(f"Error {error_message}")
            else:
                pass
    else:
        print("The ISS is near you but you cannot see it as it is daytime.")
else:
    print(f"ISS is not near you.\nCurrent location of ISS: LAT:{iss_latitude} LONG:{iss_longitude}.\nYour current location: LAT:{MY_LAT} LONG:{MY_LNG}")
