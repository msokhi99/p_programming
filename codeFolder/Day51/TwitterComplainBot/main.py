from twitter_bot import TwitterBot

test_bot=TwitterBot()
internet_speeds=test_bot.get_internet_speed()
current_upload_speed=internet_speeds[0]
current_download_speed=internet_speeds[1]

for i in range(len(internet_speeds)):
    if internet_speeds[i]=="":
        internet_speeds[i]=-1

if -1 in internet_speeds:
    print(f"Please check internet connection and try again.")
else:
    test_bot.send_tweet(up_speed=float(current_upload_speed),down_speed=float(current_download_speed))
