import smtplib as sm
import logging
import os

SENDER_EMAIL="sokhimantej99@gmail.com"
SENDER_PASSWORD="USE OWN PASSWORD"
REC_EMAIL=["bobbysokhi1@gmail.com"]

class Send_Email():
    def __init__(self,news_data,stock_percentage):
        try:
            self.news_data=news_data
            self.stock_percentage=stock_percentage
            self.stock_is_up_message=self.get_stock_is_up_msg()
            self.stock_is_down_message=self.get_stock_is_down_msg()
            if self.stock_percentage>0:
                self.email=self.send_email(self.stock_is_up_message)
            else:
                self.email=self.send_email(self.stock_is_down_message)
        except Exception as err:
            logging.error(f"Error: {err}")    

    def get_stock_is_up_msg(self):
        try:
            temp_message=f"Subject: BTC Stock Price News\n\nBTC is up {round((self.stock_percentage),2)}%. Now is a good time to invest. Here are some articles to help you make a decision:\n\n"
            for article in self.news_data["articles"]:
                    title=article["title"]
                    date_published=article["publishedAt"]
                    url=article["url"]
                    article_message=f"{title} : {date_published}\nLink: {url}\n\n"
                    temp_message+=article_message
            return temp_message
        except KeyError as err:
            logging.error(f"KeyError: {err}")
        except Exception as err:
            logging.error(f"Error: {err}")

    def get_stock_is_down_msg(self):
        try:
            temp_message=f"Subject: BTC Stock Price News\n\nBTC is down {round((self.stock_percentage),2)}%. Now is not a good time to invest. Here are some articles to help you make a decision:\n\n"
            for article in self.news_data["articles"]:
                    title=article["title"]
                    date_published=article["publishedAt"]
                    url=article["url"]
                    article_message=f"{title} : {date_published}\nLink: {url}\n\n"
                    temp_message+=article_message
            return temp_message
        except KeyError as err:
            logging.error(f"KeyError: {err}")
        except Exception as err:
            logging.error(f"Error: {err}")
    
    def send_email(self,message):
        with sm.SMTP("smtp.gmail.com",port=587) as new_connection:
            try:
                new_connection.starttls()
                new_connection.login(user=SENDER_EMAIL,password=SENDER_PASSWORD)
            except sm.SMTPAuthenticationError as err:
                logging.error(f"Authentication Error: {err}")
            else:
                try:
                    for email in REC_EMAIL:
                        new_connection.sendmail(from_addr=SENDER_EMAIL,to_addrs=email,msg=f"{message}".encode("utf8"))
                except sm.SMTPException as err:
                    logging.error(f"Error: {err}")