import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main
from tests.helpers_login import login


@pytest.fixture(autouse=True)
def open_constructor(driver, credentials):
    email, pwd = credentials
    driver.get(main.BASE_URL)
    driver.find_element(*main.MainPage.LOGIN_BTN).click()
    login(driver, email, pwd)
    WebDriverWait(driver, 10).until(EC.url_to_be(main.BASE_URL + "/"))
    driver.find_element(*main.MainPage.CONSTRUCTOR_LINK).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(main.MainPage.TAB_BUNS)
    )


def click_tab_if_needed(driver, tab):
    el = driver.find_element(*tab)
    if "tab_tab_type_current" in el.get_attribute("class"):
        return
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", el
    )
    el.click()
    WebDriverWait(driver, 10).until(
        lambda d: "tab_tab_type_current" in d.find_element(*tab).get_attribute("class")
    )
    time.sleep(1.2)  # визуальная пауза


def test_constructor_tabs(driver):
    click_tab_if_needed(driver, main.MainPage.TAB_FILLINGS)
    click_tab_if_needed(driver, main.MainPage.TAB_SAUCES)
    click_tab_if_needed(driver, main.MainPage.TAB_BUNS)  
