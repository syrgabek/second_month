class Fraction:
    def __init__(self, numerator, denumerator):
        self.numeraotr = numerator
        self.denumerator = denumerator

    def __add__(self):
        self.numeraotr += self.denumerator
        return f'Сумма двух чисел через маг метод: {fraction.numeraotr}'

    def __sub__(self):
        self.numeraotr -= self.denumerator
        return f'Разность двух чисел через маг метод: {fraction.numeraotr}'

    def __mul__(self):
        self.numeraotr *= self.denumerator
        return f'Умножение двух чисел через маг метод: {fraction.numeraotr}'

    def __floordiv__(self):
        self.numeraotr //= self.denumerator
        return f'Сумма двух чисел через маг метод: {fraction.numeraotr}'
fraction = Fraction(4,4)

print(fraction.__add__())
print(fraction.__sub__())
print(fraction.__mul__())
print(fraction.__floordiv__())
