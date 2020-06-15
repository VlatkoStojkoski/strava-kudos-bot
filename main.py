import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from decouple import config
from time import sleep

chrome_options = Options()  
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=chrome_options)
driver.get("https://www.strava.com/login")
sleep(6)

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

email.send_keys(config("EMAIL"))
sleep(1)

password.send_keys(config("PASSWORD"))
sleep(1)

password.submit()

while True:
    sleep(5)
    driver.execute_script("document.querySelectorAll('.btn-kudo[title=\"Give Kudos\"]').forEach(el=>el.click())")
    sleep(1000)
    driver.refresh()