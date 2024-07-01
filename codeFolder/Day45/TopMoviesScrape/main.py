from bs4 import BeautifulSoup
import requests

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

website_request=requests.get(URL)
website_request.raise_for_status()
data_received=website_request.text

scraper=BeautifulSoup(data_received,"html.parser")

all_movies_names=[]

movie_names=scraper.find_all(name="h3",class_="title")

for movie in movie_names:
    temp_movie_name=movie.getText()
    all_movies_names.append(temp_movie_name)

with open("/home/msokhi99/Desktop/py_programming/Day45/top_moves.txt",mode="w") as file:
    for movie in all_movies_names[::-1]:
        file.writelines(f"{movie}\n")
