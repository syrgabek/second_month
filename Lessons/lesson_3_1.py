class MusicPlayable:
    def play_music(self, song):
        print(f'Music is playing ({song})')


class Car(MusicPlayable):

    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
        print('I can drive')

    def __str__(self):
        return f'Car\n' \
               f'Model: {self.model} Year: {self.year}'

    def __del__(self):
        print('Car object was deleted')

    def __gt__(self, other):
        return self.year > other.year


class FuelCar(Car):
    __total_fuel = 500

    def __init__(self, model, year, fuel_amount):
        Car.__init__(self, model, year)
        self.__fuel_amount = fuel_amount

    @staticmethod
    def addition(num1, num2):
        print(num1 + num2)

    @classmethod
    def fill_out(cls, amount):
        cls.__total_fuel = cls.__total_fuel - amount # cls.__total_fuel -= amount
        print(f'Total fuel remain: {cls.__total_fuel}')
        return amount

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value):
        self.__fuel_amount = value

    def drive(self):
        print('I can drive using fuel engine')

    def method_of_fuel_car(self):
        pass

    def __str__(self):
        return super(FuelCar, self).__str__() \
               + f' Fuel amount: {self.fuel_amount}'

    def __add__(self, other):
        return self.fuel_amount + other.fuel_amount


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print('I can drive using electric engine')

    def method_of_electric_car(self):
        pass

    def __str__(self):
        return super(ElectricCar, self).__str__() + \
               f' Battery: {self.battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, fuel_amount, battery):
        ElectricCar.__init__(self, model, year, battery)
        FuelCar.__init__(self, model, year, fuel_amount)

    def method_of_hybrid_car(self):
        pass


class SmartPhone(MusicPlayable):
    pass


civic = HybridCar("Honda Civic", 2020, 15, 20000)
civic.drive()
civic.play_music("It's my life")

redmi = SmartPhone()
redmi.play_music("Forever young")

print(civic)

honda_car = FuelCar("Honda Accord", 2019, 25)
print(honda_car)

number_1 = 7
number_2 = 10
print(number_2 > number_1)
print(number_2 + number_1)
print(honda_car > civic)
print(honda_car + civic)

civic.fuel_amount += FuelCar.fill_out(10)

print(civic)

# print(HybridCar.mro())
