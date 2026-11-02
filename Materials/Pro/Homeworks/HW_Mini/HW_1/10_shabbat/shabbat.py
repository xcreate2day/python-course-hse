# 10. Шаббат

import functools


def shabbat(func):
    stopped = False

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal stopped
        if stopped:
            return "Отдых"
        result = func(*args, **kwargs)
        if isinstance(result, str) and len(result) == 6:
            stopped = True
            return "Отдых"
        return result

    return wrapper

# Оставляйте только декоратор shabbat.
# Для запуска тестов: python -m pytest test.py.
