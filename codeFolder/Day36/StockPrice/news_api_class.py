import requests
import logging

API_URL="https://newsapi.org/v2/top-headlines"
API_PARAMS={
    "apikey":"USE OWN KEY",
    "country":"ca",
    "category":"business"
}

class News_Api():
    def __init__(self):
        try:
            self.request_api=requests.get(url=API_URL,params=API_PARAMS)
            self.request_api.raise_for_status()
            self.requested_data=self.request_api.json()
            self.data_list=self.get_organized_data()
        except requests.exceptions.RequestException as err:
            logging.error(f"Request Failed: {err}")
        except requests.exceptions.JSONDecodeError as err:
            logging.error(f"JSON Error: {err}")
        except Exception as err:
            logging.error(f"An unexpected error occured: {err}")

    def get_organized_data(self):
        try:
            data_list={
                "articles":[]
            }
            for article in self.requested_data["articles"]:
                new_article={
                    "title":article["title"],
                    "url":article["url"],
                    "publishedAt":article["publishedAt"]
                }
                data_list["articles"].append(new_article)
            return data_list
        except Exception as err:
            logging.error(f"Error in get_organized_data: {err}")