# 2. Не передали

_MY_NOTHING = object()


def ask(answer=_MY_NOTHING):
    if answer is _MY_NOTHING:
        return "не передали"
    return answer

# Оставляйте только функцию ask.
# Для запуска тестов: python -m pytest test.py.
