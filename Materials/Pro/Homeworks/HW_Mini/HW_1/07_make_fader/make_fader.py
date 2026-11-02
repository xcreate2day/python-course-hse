# 7. Фейдер

def make_fader(level):
    def change(delta):
        nonlocal level
        level = max(0, min(100, level + delta))
        return level
    return change

# Оставляйте только функцию make_fader.
# Для запуска тестов: python -m pytest test.py.
