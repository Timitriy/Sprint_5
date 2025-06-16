from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.nomoreparties.site"

class MainPage:
    # Кнопки/ссылки в шапке
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_AREA_BTN = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    # Вкладки конструктора
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::*")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::*")
    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::*")
    CONSTRUCTOR_HEADER = (By.XPATH,"//h1[contains(text(),'Соберите бургер')]")