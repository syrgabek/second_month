# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.!!!

class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

        #  Добавить сеттеры и геттеры к существующим атрибутам.!!!
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    # Добавить в класс Computer метод make_computations,
    # # в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.!!!

    def make_computations(self):
        return f'Result of sum: {self.__cpu + self.__memory}'

    # def __str__(self):
    #     return f'Result of sum: {self.__cpu + self.__memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def info(self):
        return f'CPU of computer {self.cpu} \n' \
               f'Memory of computer {self.memory} \n'
    def __str__(self):
        return f'CPU of computer {self.cpu} \n' \
               f'Memory of computer {self.memory} \n'

# Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

# Добавить сеттеры и геттеры к существующему атрибуту.!!!

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def sims(self):
        return f'list of sim card: {list}'

    def __str__(self):
        return f'list of sim card: {list}'

# Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number,
#  в котором бы распечатывалась симуляция звонка в зависимости от переданного
# номера сим-карты (например: если при вызове метода передать число 1 и номер телефона,
#  распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).

    def call(self, sim_card_number, call_to_number):
        return f'Calling to number {call_to_number} from sim {sim_card_number}'


# Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

#     Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию проложения маршрута до локации.
    def use_gps(self, location):
        print(f'Move forward to get: {location}')

    # def info(self):
    #     return f'CPU of phone: {self.cpu} \n' \
    #            f'Memory of phone: {self.memory} \n' \


    def __str__(self):
        return f'CPU of phone {self.cpu} \n' \
               f'Memory of phone {self.memory} \n' \

# В каждом классе переопределить магический метод str которые бы возвращали полную информацию об объекте.
# Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.


computer = Computer(6, 1024)
print(computer.info())
print(computer.make_computations())
sim_1 = '1 - MegaCome'
sim_2 = '2 - Beeline'
list = [sim_1, sim_2]
phone = Phone(1)
phone.sims()

print(phone.call(list[0], 755670170))
smartphone = SmartPhone(3, 12, list)
smartphone.use_gps('Sum')
smartphone.info()

print('_______________Results of str______________')
print(computer)
print(phone)
print(smartphone)
print(computer > smartphone)

