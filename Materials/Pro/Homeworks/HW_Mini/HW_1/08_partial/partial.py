# 8. Пресет

def partial(func, /, *args, **kwargs):
    def wrapper(*new_args, **new_kwargs):
        merged_kwargs = {**kwargs, **new_kwargs}
        return func(*args, *new_args, **merged_kwargs)
    return wrapper

# Оставляйте только функцию partial.
# Для запуска тестов: python -m pytest test.py.
