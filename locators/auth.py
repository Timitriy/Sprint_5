from selenium.webdriver.common.by import By


class AuthPage:
    # Поля ввода
    NAME_INPUT     = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT    = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    # Основные кнопки
    SUBMIT_LOGIN    = (By.XPATH, "//button[text()='Войти']")
    SUBMIT_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Ссылки/кнопки навигации
    REGISTER_LINK        = (By.LINK_TEXT, "Зарегистрироваться")   # ← добавили
    LOGIN_LINK           = (By.LINK_TEXT, "Войти")                # на /register и /forgot-password
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")  # на /login
