# 5. Распаковка

def unpack(boxes):
    result = []
    for item in boxes:
        if isinstance(item, list):
            result.extend(unpack(item))
        else:
            result.append(item)
    return result

# Оставляйте только функцию unpack.
# Для запуска тестов: python -m pytest test.py.
