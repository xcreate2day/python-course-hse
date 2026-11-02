# 4. Польская запись

def polish(expr):
    if isinstance(expr, int):
        return str(expr)
    oprtr, left, right = expr
    return f"{oprtr} {polish(left)} {polish(right)}"

# Оставляйте только функцию polish.
# Для запуска тестов: python -m pytest test.py.
