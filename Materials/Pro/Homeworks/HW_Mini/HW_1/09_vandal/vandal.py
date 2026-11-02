# 9. Вредитель

import functools


def vandal(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    if wrapper.__doc__ is not None:
        wrapper.__doc__ = wrapper.__doc__[::-1]

    return wrapper

# Оставляйте только декоратор vandal.
# Для запуска тестов: python -m pytest test.py.
