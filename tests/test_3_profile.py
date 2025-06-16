import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main, profile


class TestProfile:

    def test_go_to_profile(self, logged_in):
        driver = logged_in
        driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(profile.ProfilePage.PERSONAL_DATA_TEXT)
        )
        assert "персональные данные" in driver.page_source.lower()

    def test_back_to_constructor_by_button(self, logged_in):
        driver = logged_in
        driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
        driver.find_element(*profile.ProfilePage.CONSTRUCTOR_BTN).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(main.MainPage.CONSTRUCTOR_HEADER)
        )
        assert "соберите бургер" in driver.page_source.lower()

    def test_back_to_constructor_by_logo(self, logged_in):
        driver = logged_in
        driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
        driver.find_element(*main.MainPage.LOGO).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(main.MainPage.CONSTRUCTOR_HEADER)
        )
        assert "соберите бургер" in driver.page_source.lower()

    def test_logout(self, logged_in):
        driver = logged_in
        driver.find_element(*main.MainPage.PERSONAL_AREA_BTN).click()
        
        # ждём пока кнопка станет кликабельной и кликаем
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(profile.ProfilePage.EXIT_BTN)
        ).click()
        WebDriverWait(driver, 5).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url
