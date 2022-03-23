class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_info(self):
        return (f'name {self.name} \n'
               f'age {self.age} \n'
               f'marks {self.marks}')

    def avarage(self):
        return sum(self.marks.values())/2


st1 = Student('Aman', 23, dict(physics = 5, literture = 5, english = 5))
print(st1.get_info())
print(st1.avarage())
