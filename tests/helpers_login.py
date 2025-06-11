from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import auth

def login(driver, email: str, pwd: str):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(auth.AuthPage.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*auth.AuthPage.PASSWORD_INPUT).send_keys(pwd)
    driver.find_element(*auth.AuthPage.SUBMIT_LOGIN).click()
