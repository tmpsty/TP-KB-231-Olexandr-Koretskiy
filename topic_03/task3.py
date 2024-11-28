d = {"a": 1, "b": 2, "c": 3}

d.update({"d": 4})  # Додавання ключа
print("update:", d)

del d["b"]  # Видалення ключа
print("del:", d)

d.clear()  # Очищення словника
print("clear:", d)

d = {"x": 10, "y": 20}  # Відновлення словника
print("keys:", d.keys())  # Ключі
print("values:", d.values())  # Значення
print("items:", d.items())  # Пари ключ-значення