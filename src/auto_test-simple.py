from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

link = "https://www.google.com/"
browser = webdriver.Firefox()
browser.get(link)

search = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search.send_keys("Globe")
time.sleep (1)               # I know it's a bad thing to do. But this is just a simple test..
search.send_keys(Keys.ENTER)
