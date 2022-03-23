# Урок 2 Ты самый лучший:
# Инкапсуляция
class Animal:
    # Входяцие параметры
    def __init__(self, name, age, color):
        # Атриьуты
        # Приватный атрибут self.__name
        self.name = name
        self.age = age
        self.color = color

        # 3 Создаем метод

    def info(self):
        return f'Name: {self.name} Age: {self.age} Color: {self.color}'

        # 2 Создаем обьект


some_animal = Animal('Bobik', 2, 'Brown')
print(some_animal.info())
