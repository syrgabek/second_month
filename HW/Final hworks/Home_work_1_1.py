
#1st day of python programming... HW1
# Создать класс Person с атрибутами fullname, age, is_married!!!
#
# Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке!!!

# Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks,!!!

#2который был бы словарем, где ключ это название урока, а значение - оценка.!!!

# Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам!!!

# Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.!!!

# Добавить в класс Teacher поле уровня класса salary

# Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле:!!!
# к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.!!!

# Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату!!!

# Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики
# добавляются в список и список возвращается методом как результат.

# Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике
# с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.
# Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики
# добавляются в список и список возвращается методом как результат.

# Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике
# с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.


class Person:

    # Конструктор
    def __init__(self, f, a, i):
        self.fullname = f
        self.age = a
        self.is_married = i

    # Метод
    def introduce_yourself(self):

        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} ')


man = Person('Bakyt_uulu_Amantur', 24, False)


# Student


class Student(Person):
    def __init__(self, f, a, i, marks):
        Person.__init__(self, f, a, i)
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
        return int(sum(self.marks.values())/len(self.marks))

# {'math': 5}


st1 = Student('Esen', 13, False, dict(matha=5, physics=5, english=5))


class Teacher(Person):
    salary = 21000
    # конструктор

    def __init__(self, f, a, i, e):
        Person.__init__(self, f, a, i)
        self.experience = e

    def introduce_yourself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} \n'
                f'Experience: {self.experience} ')

    # Метод считывание зарплаты
    def salary_count(self):
        if self.experience > 3:
            return ((Teacher.salary) + (self.experience - 3) * t)
        else:
            return Teacher.salary


#  Call the function
def create_students():
    st2 = Student('Aman',14 , False, dict(matha=5, physics=5, english=5))
    st3 = Student('Oleg',14 , False, dict(matha=3, physics=4, english=5))
    st4 = Student('Zholon',14 , False, dict(matha=4, physics=4, english=5))
    #  Тут я хотел сделать один длинный список но из-за длинных данных я сделал отдельный список для каждого студента
    return [f'Student: {st2.fullname}, Age: {st2.age}, Married: {st2.is_married}, Marks: {st2.get_marks()}, Avarege_mark: {st2.get_am()}'],\
           [f'Student: {st3.fullname}, Age: {st3.age}, Married: {st3.is_married}, Marks: {st2.get_marks()}, Avarege_mark: {st3.get_am()}'],\
           [f'Student: {st4.fullname}, Age: {st4.age}, Married: {st4.is_married}, Marks: {st2.get_marks()}, Avarege_mark: {st4.get_am()}']





#  Создаем обьект для класса учитель
print(man.introduce_yourself())
print('-'*40)
teach1 = Teacher("Aleksey", 37, True, 4)
t = (Teacher.salary / 100) * 5
print(st1.introduce_yourself())
print(st1.get_marks())
print(f'Avarage mark: {st1.get_am()}')
print('-'*40)
print(teach1.introduce_yourself())
print(f'Teachers salary: {int(teach1.salary_count())}')
print('='*180)
for func in [create_students]:
    x = func()
    print(x)