from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import loginInfo

import time

browser = Chrome(ChromeDriverManager().install())

browser.get("https://twitter.com/")

time.sleep(2)

login_button = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span")
login_button.click()

time.sleep(2)

username_input = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
username_input.send_keys(loginInfo.username)
forward_button = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
forward_button.click()

time.sleep(2)

phone_or_username_input = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
phone_or_username_input.send_keys(loginInfo.phone)
forward_button = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span")
forward_button.click()

time.sleep(2)

password_input = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password_input.send_keys(loginInfo.password)
login_button = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
login_button.click()

time.sleep(5)

search_button = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]")
search_button.click()

time.sleep(2)

search_input = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
search_input.send_keys("#yazilimayolver")
search_input.send_keys(Keys.ENTER)

time.sleep(5)

# NOTE You can navigate on the browser with these funcs
# browser.back() 
# browser.forward()

page_length = browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
match = False
while(match == False):
    lastCount = page_length
    time.sleep(3)
    page_length = browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
    if lastCount == page_length:
        match = True

elements = browser.find_elements(By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(3) > section > div > div > div > div > div > article > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div")

for element in elements:
    print("****************************")
    print(element.text)

time.sleep(5)

browser.close()