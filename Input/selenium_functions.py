from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from enum import Enum

class Browsers(Enum):
    Chrome = 1
    Firefox = 2
    Edge = 3
    Safari = 4

def browser_select(browsers_type):
    if (browsers_type == Browsers.Chrome):
        driver = webdriver.Chrome()
    elif (browsers_type == Browsers.Firefox):
        driver = webdriver.Firefox()
    elif (browsers_type == Browsers.Edge):
        driver = webdriver.Edge()
    elif (browsers_type == Browsers.Safari):
        driver = webdriver.Safari()
    
    return driver
