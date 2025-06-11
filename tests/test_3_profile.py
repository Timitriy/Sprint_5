import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import main, profile
from tests.helpers_login import login

# ----------  фикстура: авторизация ----------
@pytest.fixture(autouse=True)
def logged_in(driver, credentials):
    email, pwd = credentials
    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))


# ---------- 1. Переход в личный кабинет ----------
def test_go_to_profile(driver):
    driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//p[contains(@class,'Account_text') and contains(text(),'изменить свои персональные данные')]")
        )
    )
    assert "account/profile" in driver.current_url


# ---------- 2. Из ЛК → конструктор (кнопкой) ----------
def test_profile_to_constructor_button(driver):
    driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
    driver.find_element(*main.MainPage.CONSTRUCTOR_LINK).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
    )
    assert driver.current_url.rstrip("/") == main.BASE_URL.rstrip("/")


# ---------- 3. Из ЛК → конструктор (логотип) ----------
def test_profile_to_constructor_logo(driver):
    driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
    driver.find_element(*main.MainPage.LOGO).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
    )
    assert driver.current_url.rstrip("/") == main.BASE_URL.rstrip("/")


# ---------- 4. Выход из аккаунта ----------
def test_logout(driver):
    driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()

    # ждём появления кнопки «Выход» и кликаем
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(profile.ProfilePage.EXIT_BTN)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
    )
    assert "login" in driver.current_url
