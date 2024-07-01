from bs4 import BeautifulSoup
import requests

get_website_response=requests.get(url="https://news.ycombinator.com")
get_website_response.raise_for_status()
data_output=get_website_response.text

all_articles=[]
all_links=[]
all_upvotes=[]

soup=BeautifulSoup(data_output,"html.parser")
news_titles=soup.find_all(name="span",class_="titleline")
for titles in news_titles:
    article_title=titles.find(name="a").getText()
    all_articles.append(article_title)

for titles in news_titles:
    news_links=titles.find(name="a").get("href")
    all_links.append(news_links)

article_upvotes=soup.find_all(name="span",class_="score")
for upvotes in article_upvotes:
    temp_upvote=upvotes.getText()
    all_upvotes.append(int(temp_upvote.split()[0]))

max=0

for i in range(len(all_upvotes)):
    if all_upvotes[i]>max:
        max=all_upvotes[i]
        index_number=i

print(f"Highest Upvoted Article: {all_articles[index_number]}")
print(f"Link to that article: {all_links[index_number]}")
print(f"No. of upvotes: {all_upvotes[index_number]}")
