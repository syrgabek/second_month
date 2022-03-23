class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

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

    def make_computations(self):
        pass

    def __str(self):
        return f"CPU: {self.cpu} " \
               f"Memory: {self.__memory}"

    def __gt(self, other):
        return self.memory >= other.memory, \
               self.memory <= other.memory, \
               self.memory == other.memory


class Phone:
    def init(self, sim_cards_list):
        self.sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {sim_card_number} с сим-карты-{call_to_number}")

    def __str(self):
        return super(Phone, self), f" sim cards number: {self.sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init(self, cpu, memory, sim_cards_list, location):
        Computer(self, cpu, memory)
        Phone.init(self, sim_cards_list)
        self.location = location

    def use_gps(self, location):
        print(f"Локация отмечена, ведется маршрут в {location}")


pc = Computer("Ryzen 3500u", 8)
tel = Phone("+996 777 99 88 11")
smartPhone = SmartPhone("Snapdragon 888", 6, "+996 500 01 13 01", "Alamedin")
smartPhone2 = SmartPhone("MediaTech 2500", 4, "+996 555 01 23 45", "Alamedin")

# print(pc, "/n",
#       tel, '/n',
#       smartPhone, '/n',
#       smartPhone2)
print(pc)
print(tel)
print(smartPhone)
print(smartPhone2)