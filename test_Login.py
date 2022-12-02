from selenium import webdriver
import pytest
import os
from time import sleep

from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)

    else:
        driver_ = webdriver.Chrome()

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_


def test_Login(driver):
    userName = 'standard_user'
    passWord = 'secret_sauce'

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys(userName)
    sleep(3)
    driver.find_element(By.ID, 'password').send_keys(passWord)
    sleep(3)
    driver.find_element(By.ID, 'login-button').click()
    sleep(10)


def test_LoginFailed(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('andra')
    sleep(3)
    driver.find_element(By.ID, 'password').send_keys('andra')
    sleep(3)
    driver.find_element(By.ID, 'login-button').click()
    sleep(10)
