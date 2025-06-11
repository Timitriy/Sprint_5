# tests/test_register.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import auth
from faker import Faker

fake = Faker("ru_RU")

def random_email() -> str:
    return f"{fake.user_name()}_{fake.random_int(100,999)}@ya.ru"

@pytest.mark.registration
def test_success_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located(auth.AuthPage.NAME_INPUT))\
        .send_keys(fake.first_name())
    driver.find_element(*auth.AuthPage.EMAIL_INPUT).send_keys(random_email())
    driver.find_element(*auth.AuthPage.PASSWORD_INPUT).send_keys(fake.password(length=8, special_chars=False))
    driver.find_element(*auth.AuthPage.SUBMIT_REGISTER).click()

    # ожидаем редирект на /login
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url
