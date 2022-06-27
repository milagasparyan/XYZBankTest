import py_compile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from Bankingproject import Homepage




browser = webdriver.Edge(".\Bankingproject\drivers\msedgedriver.exe")
objHome = Homepage(browser)


def test_1():
    objHome.openHomePage()
    objHome.clickManagerLogin()









