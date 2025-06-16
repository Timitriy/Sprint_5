import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main, auth          
from tests.helpers_login import login


class TestLogin:

    @pytest.mark.login
    def test_login_from_main(self, driver, credentials):
        email, pwd = credentials
        driver.get(main.BASE_URL)
        driver.find_element(*main.MainPage.LOGIN_BTN).click()
        login(driver, email, pwd)

        WebDriverWait(driver, 10).until(
            EC.url_to_be(main.BASE_URL + "/")
        )
        assert driver.current_url.rstrip("/") == main.BASE_URL.rstrip("/")

    @pytest.mark.login
    def test_login_from_personal_area(self, driver, credentials):
        email, pwd = credentials
        driver.get(main.BASE_URL)
        driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
        login(driver, email, pwd)

        WebDriverWait(driver, 15).until(
            lambda d: "account/profile" in d.current_url
            or d.current_url.rstrip("/") == main.BASE_URL.rstrip("/")
        )
        assert "/account/profile" in driver.current_url or \
               driver.current_url.rstrip("/") == main.BASE_URL.rstrip("/")

    @pytest.mark.login
    def test_login_from_register_form(self, driver, credentials):
        email, pwd = credentials
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*auth.AuthPage.LOGIN_LINK).click()       
        login(driver, email, pwd)

        WebDriverWait(driver, 10).until(
            EC.url_to_be(main.BASE_URL + "/")
        )
        assert driver.current_url.rstrip("/") == main.BASE_URL.rstrip("/")

    @pytest.mark.login
    def test_login_from_forgot_password(self, driver, credentials):
        email, pwd = credentials
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*auth.AuthPage.LOGIN_LINK).click()       
        login(driver, email, pwd)

        WebDriverWait(driver, 10).until(
            EC.url_to_be(main.BASE_URL + "/")
        )
        assert driver.current_url.rstrip("/") == main.BASE_URL.rstrip("/")