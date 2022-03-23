 class Transport:
    def __init__(self, model, year, color, is_crashed):
        self.model = model
        self.year = year
        self.color = color
        self.is_crashed = is_crashed

    def move(self):
        print(f'Transport {self.model} moving')


class Yacht(Transport):
    def __init__(self, model, year, color, is_crashed=False):
        Transport.__init__(self, model, year, color, is_crashed)


class Car(Transport):
    wheels_number = 4

    def __init__(self, model, year, color, is_crashed, penalty_amount=0):
        Transport.__init__(self, model, year, color, is_crashed)
        self.penalty_amount = penalty_amount

    def drive(self, city):
        print(f'Car {self.model} driving to {city}')

    def change_color(self, new_color):
        self.color = new_color


class Truck(Car):
    wheels_number = 8

    def __init__(self, model, year, color, is_crashed,
                 penalty_amount=0, load_capacity=0):
        Car.__init__(self, model, year, color, is_crashed, penalty_amount)
        self.load_capacity = load_capacity

    def load_cargo(self, weight):
        if weight < self.load_capacity:
            print(f'Cargo is loaded to the truck {weight}')
        else:
            print(f'You can not load the cargo more than {self.load_capacity}')


winter_wheels = Car.wheels_number * 5
print("We need " + str(winter_wheels))

mazda_car = Car(model="Mazda 323", year=2002, color="Silver", is_crashed=True)
print(f'{mazda_car.model} {mazda_car.year} {mazda_car.color} '
      f'{mazda_car.is_crashed} {mazda_car.penalty_amount}')
mazda_car.color = "Green"
print(f'{mazda_car.model} {mazda_car.year} {mazda_car.color} '
      f'{mazda_car.is_crashed} {mazda_car.penalty_amount}')

bmw_car = Car("Bwm x7", 2022, "Black", False, 500)
print(f'{bmw_car.model} {bmw_car.year} {bmw_car.color} {bmw_car.is_crashed} '
      f'{bmw_car.penalty_amount} {mazda_car.wheels_number}')
bmw_car.drive("Osh")
mazda_car.drive("Miami")
bmw_car.change_color("White")
print(f'{bmw_car.model} {bmw_car.year} {bmw_car.color} {bmw_car.is_crashed} '
      f'{bmw_car.penalty_amount} {bmw_car.wheels_number}')
bmw_car.wheels_number = 5
Car.wheels_number = 5

my_yacht = Yacht("Yamaha", 2020, "White", True)
my_yacht.move()

kamaz_truck = Truck("Kamaz 3901", 1988, "Hakhi", True, 0, 30000)
print(f'{kamaz_truck.model} {kamaz_truck.year} {kamaz_truck.color} {kamaz_truck.is_crashed} '
      f'{kamaz_truck.penalty_amount} {kamaz_truck.wheels_number}')
kamaz_truck.load_cargo(9000)

