class Figure:
    unit = 'cm'
# Сверху создаал класс Figure(фигура) с атрибутом уровня класса unit(единица измерения величин)
# и присвоил ему значение cm(сантиметры)

# Ниже создал приватный атрибут perimeter в классе Figure,
# который бы по умолчанию в конструкторе присваивался к нулю.
# и в конструкторе класса Figure только 1 входящий параметр self. второй пункт выполнен!
    def __init__(self, perimetr=0):
        self.__perimetr = perimetr

# Создаал в классе Figure геттер и сеттер для атрибута perimeter.

    def perimetr(self):
        return self.__perimetr


    def set_perimetr(self, perimetr):
        if perimetr < 0:
            print('Please enter the correct number')
        else:
            self.__perimetr = perimetr

    def info(self):
        return f'{self.__perimetr}'

some_figure = Figure()
print(some_figure.info())
some_figure.set_perimetr(5)
print(some_figure.info())




