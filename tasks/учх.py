import re


class Data:

    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def data(self):
        pass


file = open('MOCK_DATA.txt', 'r')
full_name = file.read()
file = open('name.txt', mode='w', encoding='UTF-8')
search_name = r'[A-Z][A-z][A-z]+\s[A-Z][a-z|\'][A-z]+\s'\
              # r'[A-Z][A-z]+\s[a-z]+\s\w+|' \
              # r'[A-Z][A-z]+\s[A-z][A-z]+\s+|'\
              # r"[A-Z][A-z]+\s\w'\D{2}[A-z]+|" \
              # r'[A-Z][A-z|\-|\s]+\s[A-z|\'*\s][A-z][A-z|\'*\s]+\s+\.*'


result1 = re.findall(search_name, full_name)

for n in result1:
    print(n)
    file.write(n + "\n")
file.write(f"Длина: {str(len(result1))}")
print(len(result1))



