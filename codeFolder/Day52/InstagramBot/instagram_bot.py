from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException,NoSuchElementException
from dotenv import load_dotenv
import os

load_dotenv()

username=os.getenv("Username")
password=os.getenv("Password")

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

URL="https://www.instagram.com/"

class InstagramBot:
    def __init__(self):
        try:
            self.web_driver=webdriver.Chrome(options=chrome_options)
        except WebDriverException:
            print("There is a problem with the web driver. Please try again.")
    
    def sign_in_instagram(self):
        try:
            self.web_driver.get(url=URL)
        except WebDriverException:
            print("There is a problem with the web driver. Please try again.")
        except Exception:
            print("There is a problem with the URL. Please try again.")
        else:
            try:
                self.web_driver.implicitly_wait(5)
                enter_username=self.web_driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
            except NoSuchElementException:
                print("There is no such element. Please check the XPATH and try again.")
            else:
                self.web_driver.implicitly_wait(5)
                enter_username.send_keys(username + Keys.TAB + password + Keys.ENTER)
    
    def search_for_target_and_follow(self):
        self.web_driver.implicitly_wait(10)
        turn_notifications_off=self.web_driver.find_element(By.XPATH,value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        if turn_notifications_off:
                turn_notifications_off.click()
        try:
            target_account=str(input("TARGET ACCOUNT: "))
            self.web_driver.get(url=f"https://www.instagram.com/{target_account}/")
        except WebDriverException:
            print("There is a problem with the web driver. Please try again.")
        except Exception:
            print("There is a problem with the URL. Please try again.")
        else:
            try:
                self.web_driver.get(url=f"https://www.instagram.com/{target_account}/followers")
            except WebDriverException:
                print("There is a problem with the web driver. Please try again.")
            except Exception:
                print("There is a problem with the URL. Please try again.")
            else:
                follow_button=self.web_driver.find_element(By.XPATH,value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')
                follow_button.click()
        finally:
            self.web_driver.quit()