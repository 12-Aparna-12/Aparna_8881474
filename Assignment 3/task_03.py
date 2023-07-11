# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.google.co.in/")
time.sleep(3)
search_bar = driver.find_element("id","APjFqb")
search_bar.send_keys("login gmail")
search_bar.send_keys(Keys.RETURN)
#search_bar.click()
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
selenium_link = driver.find_element("xpath","//*[@id='rso']/div[1]/div/div/div[1]/div/a/div")
selenium_link.click()
time.sleep(5)
email = driver.find_element("id","identifierId")
email.send_keys("aparna123")
time.sleep(5)
email.send_keys(Keys.ENTER)
time.sleep(5)
next_button = driver.find_element("xpath","//*[@id='next']/div/div/a")
next_button.click()
email1 = driver.find_element("id","identifierId")
email1.send_keys("aparnabadugu")
email1.send_keys(Keys.ENTER)
time.sleep(5)
#email.send_keys(Keys.RETURN)
driver.close()
