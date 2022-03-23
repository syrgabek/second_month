import os
from random import randint, choice
from calculator import addition as add_two_numbers
from person import Person
from termcolor import cprint
from envparse import env
print(randint(1, 5))
print(add_two_numbers(2, 4))
man = Person('John', 23)
cprint(man, 'red')

user_name = os.environ.get('DB_USER')
user_pass = '123123456'
print(user_name)

env.read_envfile('vars.env')
t = os.environ.get('PYTHON')
print(t)