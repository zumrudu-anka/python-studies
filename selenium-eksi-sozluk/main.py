from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
import time
import random

browser = webdriver.Chrome()

# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])

BASE_URL = f"https://eksisozluk2023.com/mustafa-kemal-ataturk--34712"
browser.get(BASE_URL)
time.sleep(5)
maxPageNumber = int(browser.find_element(By.CSS_SELECTOR, "#topic > div.clearfix.sub-title-container > div.pager > a.last").text)
print(maxPageNumber)

pageSampleCount = 1
entries = []
while pageSampleCount < 11:
    randomPage = random.randint(1, maxPageNumber)
    randomPageUrl = f"https://eksisozluk2023.com/mustafa-kemal-ataturk--34712?p={randomPage}"
    browser.get(randomPageUrl)
    time.sleep(3)
    elements = browser.find_elements(By.CSS_SELECTOR, ".content")
    for element in elements:
        entries.append(element.text)
    pageSampleCount += 1

with open("entries.txt", "w", encoding = "UTF-8") as file:
    for index, entry in enumerate(entries):
        file.write(f"{index + 1}.\n{entry}\n")
        file.write("*********************\n")

browser.close()
