from faker import Faker

fake = Faker("ru_RU")


def random_email() -> str:
    """Генерирует уникальный email в требуемом формате."""
    base = f"{fake.first_name().lower()}{fake.last_name().lower()}_{fake.random_int(100, 999)}"
    return f"{base}@ya.ru"


def random_password() -> str:
    """Пароль ≥ 6 символов: буквы + цифры."""
    return fake.password(length=10, special_chars=False)