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


def test_CO(driver):
    driver.get("https://www.saucedemo.com/")
    userName = 'standard_user'
    passWord = 'secret_sauce'

    driver.find_element(By.ID, 'user-name').send_keys(userName)
    sleep(3)
    driver.find_element(By.ID, 'password').send_keys(passWord)
    sleep(3)
    driver.find_element(By.ID, 'login-button').click()
    sleep(10)
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    sleep(2)
    driver.find_element(By.ID, 'shopping_cart_container').click()
    sleep(2)
    driver.find_element(By.ID, 'checkout').click()
    sleep(2)
    driver.find_element(By.ID, 'first-name').send_keys('a')
    sleep(2)
    driver.find_element(By.ID, 'last-name').send_keys('a')
    sleep(2)
    driver.find_element(By.ID, 'postal-code').send_keys('1')
    sleep(2)
    driver.find_element(By.ID, 'continue').click()
    sleep(2)
    driver.find_element(By.ID, 'finish').click()
    sleep(2)
