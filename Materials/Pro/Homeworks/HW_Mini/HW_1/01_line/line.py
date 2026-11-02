# 1. Эфирная строка

def line(title, /, *artists, year=None):
    result = title
    if artists:
        result += " - " + ", ".join(artists)
    if year is not None:
        result += f" ({year})"
    return result

# Оставляйте только функцию line.
# Для запуска тестов: python -m pytest test.py.
