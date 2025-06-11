import pytest
from locators import main, auth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.helpers_login import login


@pytest.mark.login
def test_login_from_main(driver, credentials):
    email, pwd = credentials
    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))


@pytest.mark.login
def test_login_from_personal_area(driver, credentials):
    email, pwd = credentials
    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))
    driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
    WebDriverWait(driver, 10).until(EC.url_contains("account/profile"))


@pytest.mark.login
def test_login_from_register_form(driver, credentials):
    email, pwd = credentials
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*auth.AuthPage.LOGIN_LINK).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))


@pytest.mark.login
def test_login_from_forgot_password(driver, credentials):
    email, pwd = credentials
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*auth.AuthPage.LOGIN_LINK).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))
