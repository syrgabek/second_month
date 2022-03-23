class Person:
    # Конструктор
    def __init__(self, f, a, im):
        self.fullname = f
        self.age = a
        self.is_married = im
    # Метод
    def introduce_yourself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} ')
man = Person('Bakyt_uulu_Amantur', 24, False)

# Student
class Student(Person):
    def __init__(self, f, a, im, marks: dict):
        Person.__init__(self, f, a, im)
        self.marks = marks

    # Метод
    def introduce_yourself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} ')
    def get_marks(self):
        return self.marks
    # Метод
    def get_am(self):
        return int(sum(self.marks.values())/3)

# {'math': 5}
st1 = Student('Esen', 13, False, dict(matha = 5, physics= 5,english = 5))




class Teacher(Person):
    salary = 9000
    # конструктор
    def __init__(self, f, a, i, e):
        Person.__init__(self, f, a, i)
        self.experience = e


    def introduce_yourself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} \n'
                f'Experience: {self.experience} ')

    def salary_count(self):
        if self.experience > 3:
            return ((Teacher.salary) + (self.experience - 3) * t)
        else:
            return Teacher.salary


def create_students():
    st2 = ['Aman', 14, False, {'matha':5 ,'physics': 5 , 'english': 5}]
    st3 = ['Oleg', 14, False, dict(matha=3, physics=4, english=5)]
    st4 = ['Zholon', 14, False, dict(matha=4, physics=4, english=5)]
    return(list[st2, st3, st4])


for func in [create_students]:
    # list.append('kiwi')
    x = func()
    print(x)

teach1 = Teacher("Aleksey", 37, True, 4)
t = (Teacher.salary / 100) * 5

print(man.introduce_yourself())
print(st1.introduce_yourself())
print(st1.get_marks())
print(f'Avarage mark: {st1.get_am()}')
print(teach1.introduce_yourself())
print(f'Teachers salary: {int(teach1.salary_count())}')
