class Fraction:

    def __init__ (self, numerator , denumerator):
        self.num=numerator
        self.denum=denumerator

    def show(self):
        print(self.num , self.denum)

    def __add__(self, otherfraction ):
        a = self.num * otherfraction.denum + self.denum * otherfraction.num
        b = self.denum * otherfraction.denum
        print("magic method add")
        return (f'{a} + {b}')

    def __sub__(self,otherfraction):
        a = self.num * otherfraction.denum - self.denum * otherfraction.num
        b = self.denum * otherfraction.denum
        print("magic method sub")
        return (f'{a} - {b}')

    def __mul__(self,otherfraction):
        a = self.num * otherfraction.denum * self.denum * otherfraction.num
        b = self.denum * otherfraction.denum
        print("magic method mul")
        return (f'{a} * {b}')

    def __floordiv__(self,otherfraction):
        a = self.num * otherfraction.denum // self.denum * otherfraction.num
        b = self.denum * otherfraction.denum
        print("magic method sub")
        return (f'{a} // {b}')

x = Fraction(3,5)
y = Fraction(1,4)
v = x * y

print(x.__add__)
print(y.__sub__)
print(x.__mul__)
print(y.__floordiv__)

