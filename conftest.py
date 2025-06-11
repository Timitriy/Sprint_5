# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main, auth
from utils.data import random_email, random_password


def _make_driver(browser: str = "chrome"):
    if browser == "firefox":
        return webdriver.Firefox(service=webdriver.firefox.service.Service(
            GeckoDriverManager().install()))
    return webdriver.Chrome(service=webdriver.chrome.service.Service(
        ChromeDriverManager().install()))


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox"], help="Браузер для тестов")


# ---------- 1. driver (function-scope) ----------
@pytest.fixture
def driver(request):
    drv = _make_driver(request.config.getoption("--browser"))
    drv.maximize_window()
    yield drv
    drv.quit()


# ---------- 2. credentials (также function-scope) ----------
@pytest.fixture
def credentials(driver):
    """Регистрируем нового пользователя и возвращаем (email, password)."""
    email, pwd = random_email(), random_password()

    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    driver.find_element(*auth.AuthPage.REGISTER_LINK).click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(auth.AuthPage.NAME_INPUT)).send_keys("Auto")
    driver.find_element(*auth.AuthPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*auth.AuthPage.PASSWORD_INPUT).send_keys(pwd)
    driver.find_element(*auth.AuthPage.SUBMIT_REGISTER).click()

    return email, pwd
