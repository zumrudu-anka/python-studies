from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import loginInfo

browser = Chrome(ChromeDriverManager().install())
browser.get("https://www.instagram.com/")

time.sleep(2)

username_input = browser.find_element(By.NAME, "username")
username_input.send_keys(loginInfo.username)

password_input = browser.find_element(By.NAME, "password")
password_input.send_keys(loginInfo.password)

login_button = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")
login_button.click()

time.sleep(5)

profile_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a")
profile_button.click()

time.sleep(3)

followers_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
followers_button.click()

time.sleep(5)
js_command = """
function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

const followers_div = getElementByXpath('/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]');
followers_div.scrollTo(0, followers_div.scrollHeight);
let followers_div_length = followers_div.scrollHeight;
return followers_div_length;
"""

page_length = browser.execute_script(js_command)
match = False
while(match == False):
    lastCount = page_length
    time.sleep(3)
    page_length = browser.execute_script(js_command)
    if lastCount == page_length:
        match = True

time.sleep(5)

followers_outer_div = browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")
followers = followers_outer_div.find_elements(By.CSS_SELECTOR, "div > div > div > div > div > div > div > div > div > div > a > div > div > span")

follower_usernames = list()

for follower in followers:
    follower_usernames.append(follower.text)

with open("followers.txt", "w", encoding="UTF-8") as followers_file:
    for follower_username in follower_usernames:
        followers_file.write(follower_username + "\n")

followers_close_button = browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
followers_close_button.click()

time.sleep(2)

follows_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")
follows_button.click()

time.sleep(5)
js_command = """
function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

const follows_div = getElementByXpath('/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]');
follows_div.scrollTo(0, follows_div.scrollHeight);
let follows_div_length = follows_div.scrollHeight;
return follows_div_length;
"""

page_length = browser.execute_script(js_command)
match = False
while(match == False):
    lastCount = page_length
    time.sleep(3)
    page_length = browser.execute_script(js_command)
    if lastCount == page_length:
        match = True

time.sleep(5)

follows_outer_div = browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div")
follows = follows_outer_div.find_elements(By.CSS_SELECTOR, "div > div > div > div > div > div > div > div > div > div > a > div > div > span")

follows_usernames = list()

for follow in follows:
    follows_usernames.append(follow.text)

with open("follows.txt", "w", encoding="UTF-8") as follows_file:
    for follow_username in follows_usernames:
        follows_file.write(follow_username + "\n")

time.sleep(10)

browser.close()