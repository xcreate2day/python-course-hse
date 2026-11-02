# 6. Одна частота

FREQ = 100


def listen():
    return FREQ


def tune(delta):
    global FREQ
    FREQ += delta
    return FREQ

# Оставляйте только FREQ, listen и tune.
# Для запуска тестов: python -m pytest test.py.
