from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchDriverException,NoSuchElementException,ElementNotInteractableException
from time import sleep
from dotenv import load_dotenv
import os
from constants import PROMISED_UPLOAD_SPEED
from constants import PROMISED_DOWNLOAD_SPEED

load_dotenv()

TWITTER_USERNAME=os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD=os.getenv("TWITTER_PASSWORD")

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

SPEED_TEST_URL="https://www.speedtest.net/"
X_URL="https://www.x.com"

class TwitterBot:
    def __init__(self):
        try:
            self.web_driver=webdriver.Chrome(options=chrome_options)
        except NoSuchDriverException:
            print(f"This driver does not exist. Please check the driver and try again.")
            self.web_driver.quit()
    
    def get_internet_speed(self):
        try:
            self.web_driver.get(url=SPEED_TEST_URL)
        except NoSuchDriverException:
            print(f"This driver does not exist. Please check the driver and try again.")
            self.web_driver.quit()
        except Exception:
            print(f"Please check the URL and try again.")
            self.web_driver.quit()
        else:
            try:
                self.web_driver.implicitly_wait(time_to_wait=5)
                go_button=self.web_driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
            except NoSuchElementException:
                print("This element does not exist. Please check the selector and try again.")
                self.web_driver.quit()
            else:
                go_button.click()
                # self.web_driver.implicitly_wait(time_to_wait=45)
                sleep(40)
                download_speed=self.web_driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
                upload_speed=self.web_driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
                return download_speed,upload_speed

    def send_tweet(self,up_speed,down_speed):
        try:
            self.web_driver.get(url=X_URL)
        except NoSuchDriverException:
            print(f"This driver does not exist. Please check the driver and try again.")
        except Exception:
            print(f"Please check the URL and try again.")
        else:
            self.web_driver.implicitly_wait(5)
            try:
                x_button=self.web_driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div[1]/div/div/div/button')
            except ElementNotInteractableException:
                print(f"Driver cannot interact with element. Please check XPATH and try again.")
            else:
                x_button.click()
                self.web_driver.implicitly_wait(5)
                try:
                    sign_in_button=self.web_driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div')
                except ElementNotInteractableException:
                    print(f"Driver cannot interact with element. Please check XPATH and try again.")
                else:
                    sign_in_button.click()
                    self.web_driver.implicitly_wait(5)
                    try:
                        input_username=self.web_driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
                    except ElementNotInteractableException:
                        print(f"Driver cannot interact with element. Please check XPATH and try again.")
                    else:
                        input_username.send_keys(TWITTER_USERNAME)
                        input_username.send_keys(Keys.ENTER)
                        self.web_driver.implicitly_wait(5)
                    try:
                        input_password=self.web_driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                    except ElementNotInteractableException:
                        print(f"Driver cannot interact with element. Please check XPATH and try again.")
                    else:
                        input_password.send_keys(TWITTER_PASSWORD)
                        input_password.send_keys(Keys.ENTER)
                        self.web_driver.implicitly_wait(10)
                        if up_speed<PROMISED_UPLOAD_SPEED or down_speed<PROMISED_DOWNLOAD_SPEED:
                            try:
                                input_text=self.web_driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
                            except ElementNotInteractableException:
                                print(f"Driver cannot interact with element. Please check XPATH and try again.")
                            else:
                                input_text.send_keys(f"My Internet Speed is {up_speed}/{down_speed} which is not the promised speed of {PROMISED_UPLOAD_SPEED}/{PROMISED_DOWNLOAD_SPEED}. I want a refund.")
                                self.web_driver.implicitly_wait(10)
                                try:
                                    post_button=self.web_driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
                                except ElementNotInteractableException:
                                    print(f"Driver cannot interact with element. Please check XPATH and try again.")
                                else:
                                    post_button.click()
                        else:
                            print("Internet Speeds are OK.")
        finally:
            # self.web_driver.quit()
            pass