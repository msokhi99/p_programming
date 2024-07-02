from bs4 import BeautifulSoup
import requests
import smtplib as sm
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL=os.getenv("email_username")
PASSWORD=os.getenv("email_password")
SENDER_EMAIL="bobbysokhi1@gmail.com"

URL="https://www.amazon.ca/LG-UltragearTM-Monitor-Refresh-Response/dp/B0CV1WNF1Q/ref=sr_1_2_sspa"

HEADERS={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

def get_data(website_url):
    try:
        get_response=requests.get(url=website_url,headers=HEADERS)
        get_response.raise_for_status()
    except requests.RequestException:
        print(f"Encountered an error. Please check the URL.")
        return None
    else:
        data_output=get_response.text
        return data_output

def begin_scraping(data_to_scrape):
    scrape_machine=BeautifulSoup(data_to_scrape,"html.parser")
    return scrape_machine

def get_whole_price(scrape_machine):
    try:
        whole_price=scrape_machine.find(name="span",class_="a-price-whole").getText()
    except ValueError:
        print(f"No price found. Please check the URL.")
    else:
        return whole_price

def send_email(product_price):
    with sm.SMTP("smtp.gmail.com",port=587) as new_email:
        new_email.starttls()
        try:
            new_email.login(user=EMAIL,password=PASSWORD)
        except sm.SMTPAuthenticationError:
            print(f"Please check login credentials.")
        else:
            price_drop=product_price-300
            if product_price==price_drop:
                try:
                    new_email.sendmail(from_addr=EMAIL,to_addrs=SENDER_EMAIL,
                                        msg=f"Subject:Monitor Price Drop Alert\n\nThe price has now dropped to {price_drop} from {product_price}. Buy now.")
                except sm.SMTPResponseException:
                    print("An error occured during email. Please try again later.")
                else:
                    print("Email sent succesfully.")
            else:
                print(f"Current Price: ${product_price} which is the same as starting price. Email not sent.")

website_data=get_data(website_url=URL)
scrape_website=begin_scraping(data_to_scrape=website_data)
whole_price=get_whole_price(scrape_machine=scrape_website).replace(",","").replace(".","")
whole_price=int(whole_price)
send_email(whole_price)
