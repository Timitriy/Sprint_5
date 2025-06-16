from faker import Faker

_fake = Faker("ru_RU")

def random_email() -> str:
    """Уникальный e-mail вида ivan_123@ya.ru"""
    return f"{_fake.user_name()}_{_fake.random_int(100, 999)}@ya.ru"

def random_password(min_len: int = 8) -> str:
    return _fake.password(length=max(min_len, 6), special_chars=False)
