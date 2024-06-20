import random

'''CHALLENGE 1'''

fruits_list=["Apple","Orange","Pear"]
def make_pie(index):
    try:
        pie_to_make=fruits_list[index]
    except:
        print(f"Fruit Pie.")
    else:
        print(f"{pie_to_make} Pie.")

make_pie(random.randint(1,4))

'''CHALLENGE 2'''
import fb_dictionary

total_likes=0
fb_collection=fb_dictionary.random_dict
for post in fb_collection:
    try:
        total_likes+=post["Likes"]
    except:
        total_likes+=0

print(f"Total Likes: {total_likes}")
