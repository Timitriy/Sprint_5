import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from locators import main


@pytest.mark.usefixtures("constructor_page")          # фикстура из conftest.py
class TestConstructorTabs:
    """Три теста: Булки (default) → Соусы → Начинки."""

    # ───────── helpers ─────────
    @staticmethod
    def _is_active(driver, tab):
        """У задания активная вкладка имеет класс tab_tab_type_current."""
        return "tab_tab_type_current" in driver.find_element(*tab).get_attribute("class")

    @staticmethod
    def _click(driver, tab):
        """Клик по вкладке с гарантированным скроллом и ожиданием активации."""
        el = driver.find_element(*tab)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        ActionChains(driver).move_to_element(el).pause(0.1).click(el).perform()
        WebDriverWait(driver, 5).until(
            lambda d: TestConstructorTabs._is_active(d, tab)
        )

    # ───────── tests ──────────
    def test_default_tab_is_buns(self, driver):
        """При открытии конструктора по умолчанию активны «Булки»."""
        assert self._is_active(driver, main.MainPage.TAB_BUNS)

    def test_switch_to_sauces(self, driver):
        """Переключаемся на вкладку «Соусы»."""
        self._click(driver, main.MainPage.TAB_SAUCES)
        assert self._is_active(driver, main.MainPage.TAB_SAUCES)

    def test_switch_to_fillings(self, driver):
        """Переключаемся на вкладку «Начинки»."""
        self._click(driver, main.MainPage.TAB_FILLINGS)
        assert self._is_active(driver, main.MainPage.TAB_FILLINGS)
