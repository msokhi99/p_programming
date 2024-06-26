import requests
from date_and_time_class import Date_And_Time
import logging
import os
API_URL="https://www.alphavantage.co/query"
API_PARAMS={
    "function":"DIGITAL_CURRENCY_DAILY",
    "symbol":"BTC",
    "market":"EUR",
    "apikey":"USE OWN KEY",
}

class Stock_Api(Date_And_Time):
    def __init__(self):
        super().__init__()
        try:
            self.request_api=requests.get(url=API_URL,params=API_PARAMS)
            self.request_api.raise_for_status()
            self.requested_data=self.request_api.json()
            self.stock_price_for_yesterday=self.get_stock_price_for_yesterday()
            self.stock_price_for_day_before_yesterday=self.get_stock_price_for_day_before_yesterday()
        except requests.exceptions.RequestException as err:
            logging.error(f"Request Failed: {err}")
        except requests.exceptions.JSONDecodeError as err:
            logging.error(f"JSON Error: {err}")
        except Exception as err:
            logging.error(f"An unexpected error occured: {err}")

    def get_stock_price_for_yesterday(self):
        try:
            yesterday_stock_price=self.requested_data["Time Series (Digital Currency Daily)"][self.get_yesterday_date()]["4. close"]
            return float(yesterday_stock_price)
        except KeyError as err:
            logging.error(f"Keyerror: {err}")

    def get_stock_price_for_day_before_yesterday(self):
        try:
            day_before_yesterday_stock_price=self.requested_data["Time Series (Digital Currency Daily)"][self.get_day_before_yesterday_date()]["4. close"]
            return float(day_before_yesterday_stock_price)
        except KeyError as err:
            logging.error(f"Keyerror: {err}")