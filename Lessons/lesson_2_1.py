 from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, color):
        self._created_animal()
        self.__name = name
        self.__age = age
        self.__color = color

    @abstractmethod
    def speak(self):
        pass

    def _created_animal(self):
        print("New animal is created")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 15:
            print("Wrong value for name it must be less than 15 characters")
        else:
            self.__name = name

    @property
    def color(self):
        return self.__color

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age <= 0:
            print("Wrong value for age, it must be positive number")
        else:
            self.__age = new_age

    def info(self):
        return f'Name: {self.__name} Age: {self.__age} Color: {self.__color}'


class Cat(Animal):
    def __init__(self, name, age, color, lives):
        Animal.__init__(self, name, age, color)
        self.__lives = lives
        self._created_animal()

    def info(self):
        return super().info() + f' Lives: {self.__lives}'

    def speak(self):
        print("Cat says meow")


class Dog(Animal):
    def __init__(self, name, age, color):
        Animal.__init__(self, name, age, color)

    def speak(self):
        print("Dog says gav")


# some_animal = Animal("Bobik", 2, "Brown")
# print(some_animal.info())
# some_animal.set_age(-5)
# print(some_animal.info())
# some_animal.set_age(8)
# print(some_animal.info())
# # print(some_animal.__color)
# some_animal.name = "Barsiksdfsdfdsfsdfsdfsdfdsfsdf"
# print(some_animal.name)
tom_cat = Cat("Tom", 3, "Blue", 9)
print(tom_cat.info())

dog_bars = Dog("Barsik", 5, "Black")

list = [tom_cat, dog_bars]

for obj in list:
    obj.speak()
