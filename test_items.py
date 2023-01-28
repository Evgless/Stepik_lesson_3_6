#import pytest
#from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_exist_basket_button(browser):
    browser.get(link)
    print('\nfind button...')
    button = browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    #print(button)
    assert button, 'Button not found!'
    print('\nButton found, test PASSED')