class Figure:
    unit = 'cm'
# Сверху создаал класс Figure(фигура) с атрибутом уровня класса unit(единица измерения величин)
# и присвоил ему значение cm(сантиметры)

# Ниже создал приватный атрибут perimeter в классе Figure,
# который бы по умолчанию в конструкторе присваивался к нулю.
# и в конструкторе класса Figure только 1 входящий параметр self. второй пункт выполнен!
    def __init__(self):
        self.__perimeter = 0

# Создаал в классе Figure геттер и сеттер для атрибута perimeter.
    def get_perimeter(self):
        return self.__perimeter

    def set_perimeter(self, perimeter):
        if perimeter < 0:
            print('Please enter the correct number')
        else:
            self.__perimeter = perimeter




# Далее добавил в класс Figure нереализованный
# публичный метод calculate_area(подсчет площади фигуры)

    def calculate_area(self):
        pass

# Затем добавил в класс Figure нереализованный приватный метод calculate_perimeter(подсчет периметра фигуры)

    def calculate_perimeter(self):
        pass
# Иии добавил в класс Figure нереализованный публичный метод info(вывод полной информации о фигуре)

    def info(self):
        pass

# Создал класс Square(квадрат) и наследовал его от класса Figure.
# Добавил в класс Square атрибут side_length(длина одной стороны квадрата), атрибут сделал приватным
# В конструктор
# е класса Square должен высчитываться периметр квадрата,
# посредством вызова метода calculate_perimeter и
# возвращаемый результат метода задавался бы атрибуту perimeter.


class Square(Figure):
    def __init__(self, side_length=5):
        Figure.__init__(self)
        self.__side_length = side_length
        self.__perimeter = (self.__side_length + self.__side_length + self.__side_length + self.__side_length)
    # В классе Square переопределить метод calculate_area, который бы считал и возвращал площадь квадрата.

    def calculate_perimeter(self):
        return f' Perimeter of square: {self.__perimeter} {Figure.unit}'

    # 12. В классе Square переопределить метод calculate_perimeter, который бы считал и возвращал периметр квадрата.
    def calculate_area(self):
        return f'Square of square: {self.__side_length * self.__side_length} {Figure.unit}'

    # 13. В классе Square переопределить метод info, который бы распечатывал всю информацию о квадрате следующим образом:
    def info(self):
        return f'Square side length:{self.__side_length} {Figure.unit}\n'\
               f'{self.calculate_perimeter()}  \n'\
               f'{self.calculate_area()} '


# Создать класс Rectangle(прямоугольник), наследовать его от класса Figure.
# Добавить в класс Rectangle атрибут length(длина) и width(ширина), атрибуты должны быть приватными.
class Rectangle(Figure):
    def __init__(self, length=5, width=2):
        Figure.__init__(self)
        self.__length = length
        self.__width = width
        self.__perimeter = ((self.__width + self.__length)*2)

    def calculate_perimeter(self):
        return f'Perimeter of Rectangle: {self.__perimeter} {Figure.unit}'

    def calculate_area(self):
        return f'Square of Rectangle: {self.__length * self.__width} {Figure.unit}'

    def info(self):
        return f'Rectangle length: {self.__length} {Figure.unit} \n'\
               f'Rectangle width: {self.__width} {Figure.unit} \n' \
               f'{self.calculate_perimeter()}  \n' \
               f'{self.calculate_area()} '

# В исполняемом файле создать список из 2-х разных квадратов и 3-х разных прямоугольников
# Затем через цикл вызвать у всех объектов списка метод info


print('+++++++++++++++++++++++++++SQUARE++++++++++++++++++++++++++++++')
square = Square()
square.calculate_perimeter()
square.calculate_area()
square.info()
print(square.info())
print('=========================SQUARE_END============================')


print('==========================ReCtAnGlE==========================')
rectangle = Rectangle()
rectangle.calculate_perimeter()
rectangle.calculate_area()
rectangle.info()
print(rectangle.info())
print('=========================ReCtAnGlE EnD==========================')

sqrt = Square(5)
sqrt1 = Square(2)
# print(sqrt.info(), '\n', '______________________________________________', '\n', sqrt1.info(), '\n', '______________________________________________')

rect = Rectangle(2, 4)
rect1 = Rectangle(3, 6)
rect2 = Rectangle(4, 8)
# print(f'{rect.info()} \n  {rect1.info()} \n  {rect2.info()}')

list = [sqrt, sqrt1, rect, rect1, rect2]

for obj in list:
    print(f' ___________Square 1____________\n'
          f'{sqrt.info()}\n' 
          f' ___________Square 2____________\n'
          f'{sqrt1.info()}\n' 
          f' ___________Rectangle 1____________\n'
          f'{rect.info()}\n'
          f' ___________Rectangle 2____________\n'
          f'{rect1.info()} \n'
          f' ___________Rectangle 3____________\n'
          f'{rect2.info()}')
    break
