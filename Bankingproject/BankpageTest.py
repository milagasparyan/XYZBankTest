import py_compile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from Bankingproject import Bankpage

browser = webdriver.Edge(".\Bankingproject\drivers\msedgedriver.exe")
objBank = Bankpage(browser)

firstName = "Mila"
lastName = "Gasparyan"
postCode = 1111

def test_2():
    objBank.openBankpage()
    objBank.clickaddCustomerButton()


def test_3():
    objBank.fillFields()

def test_4():
    objBank.clickcustomersButton(firstName, lastName, postCode)
    objBank.searchCustomer(firstName, lastName, postCode)
    is_displayed_element = browser.find_element(objBank.deleteButton).is_displayed()
    assert (is_displayed_element == True)

def test_5():
    objBank.searchCustomer(firstName, lastName, postCode)
    objBank.clickDeleteButton()
    objBank.searchCustomer(firstName, lastName, postCode)
    is_displayed_element = browser.find_element(objBank.deleteButton).is_displayed()
    assert (is_displayed_element == False)

            