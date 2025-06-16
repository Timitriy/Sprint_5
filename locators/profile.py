from selenium.webdriver.common.by import By


class ProfilePage:
    #EXIT_BTN = (By.XPATH, "//button[text()='Выход']")
    INFO_TEXT     = (By.XPATH, "//p[contains(text(),'вы можете изменить свои персональные данные')]")
    LOGIN_HEADER  = (By.XPATH, "//h2[text()='Вход']")
    PERSONAL_DATA_TEXT = (By.XPATH,"//p[contains(text(),'В этом разделе')]")
    CONSTRUCTOR_BTN = (By.XPATH,"//p[text()='Конструктор']")
    EXIT_BTN = (By.XPATH,"//button[contains(text(),'Выход')]")