# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import main, auth
from tests.helpers_login import login          
from utils.data import random_email, random_password


# ---------- инструменты браузера ----------
def _make_driver(browser: str = "chrome"):
    if browser == "firefox":
        return webdriver.Firefox(
            service=webdriver.firefox.service.Service(GeckoDriverManager().install())
        )
    return webdriver.Chrome(
        service=webdriver.chrome.service.Service(ChromeDriverManager().install())
    )


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Браузер для тестов",
    )


# ---------- 1. driver (function-scope) ----------
@pytest.fixture
def driver(request):
    drv = _make_driver(request.config.getoption("--browser"))
    drv.maximize_window()
    yield drv
    drv.quit()


# ---------- 2. credentials (function-scope) ----------
@pytest.fixture
def credentials(driver):
    """Регистрируем нового пользователя и возвращаем (email, password)."""
    email, pwd = random_email(), random_password()

    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    driver.find_element(*auth.AuthPage.REGISTER_LINK).click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(auth.AuthPage.NAME_INPUT)).send_keys(
        "Auto"
    )
    driver.find_element(*auth.AuthPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*auth.AuthPage.PASSWORD_INPUT).send_keys(pwd)
    driver.find_element(*auth.AuthPage.SUBMIT_REGISTER).click()

    return email, pwd


# ---------- 3. logged_in — общий «уже авторизованный» driver ----------
@pytest.fixture
def logged_in(driver, credentials):
    """Возвращает WebDriver с авторизованным пользователем."""
    email, pwd = credentials
    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    login(driver, email, pwd)

    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))
    return driver

@pytest.fixture
def logged_in(driver, credentials):
    """Возвращает уже авторизованный driver."""
    email, pwd = credentials
    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))
    return driver

# ---------- 4. constructor — общий ----------

@pytest.fixture
def constructor_page(driver, credentials):
    """
    Авторизация и переход в «Конструктор».
    Гарантируем, что вкладка «Булки» активна (дефолт).
    """
    email, pwd = credentials
    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(main.BASE_URL + "/")
    )
    driver.find_element(*main.MainPage.CONSTRUCTOR_LINK).click()
    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in
        d.find_element(*main.MainPage.TAB_BUNS).get_attribute("class")
    )
    yield driver        