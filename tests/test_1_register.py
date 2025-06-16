import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import auth
from utils.data import random_email, random_password
class TestRegister:
    @pytest.mark.registration
    def test_success_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.visibility_of_element_located(auth.AuthPage.NAME_INPUT)
        ).send_keys("Автотест")
        driver.find_element(*auth.AuthPage.EMAIL_INPUT).send_keys(random_email())
        driver.find_element(*auth.AuthPage.PASSWORD_INPUT).send_keys(random_password())
        driver.find_element(*auth.AuthPage.SUBMIT_REGISTER).click()

        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
