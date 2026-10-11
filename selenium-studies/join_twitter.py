from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
load_dotenv()

TWITTER_USERNAME = os.getenv("TWITTER_USERNAME", "Your UserName")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD", "Your Password")

CUSTOM_OPTIONS = {
    "main_url" : "https://twitter.com",
    "elements_xpaths" : {
        "login_button" : "/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span",
        "username_input" : "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input",
        "next_button" : "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span",
        "password_input" : "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        "login_complete_button" : "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span"
    }
}

browser = webdriver.Firefox()

browser.get(CUSTOM_OPTIONS["main_url"])

time.sleep(5)

login_button = browser.find_element(By.XPATH, CUSTOM_OPTIONS["elements_xpaths"]["login_button"])
login_button.click()

time.sleep(2)

username_input = browser.find_element(By.XPATH, CUSTOM_OPTIONS["elements_xpaths"]["username_input"])
username_input.send_keys(TWITTER_USERNAME)

next_button = browser.find_element(By.XPATH, CUSTOM_OPTIONS["elements_xpaths"]["next_button"])
next_button.click()

time.sleep(2)

password_input = browser.find_element(By.XPATH, CUSTOM_OPTIONS["elements_xpaths"]["password_input"])
password_input.send_keys(TWITTER_PASSWORD)

login_complete_button = browser.find_element(By.XPATH, CUSTOM_OPTIONS["elements_xpaths"]["login_complete_button"])
login_complete_button.click()

time.sleep(10)

browser.close()