'''
Currently, this program just follows a single person. To follow multiple, 
go into the instagram_bot class and insert a for loop for range(x).

Instagram is very good at suspecting bot behaviour so use an IP.
'''

from instagram_bot import InstagramBot

test_bot=InstagramBot()
test_bot.sign_in_instagram()
test_bot.search_for_target_and_follow()
