from selenium import webdriver
import chromedriver_binary
from time import sleep

from selenium.webdriver.common.by import By

userName = 'standard_user'
passWord = 'secret_sauce'

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, 'user-name').send_keys(userName)
sleep(3)
driver.find_element(By.ID, 'password').send_keys(passWord)
sleep(3)
driver.find_element(By.ID, 'login-button').click()
sleep(10)

print("Logged is Successfully")
