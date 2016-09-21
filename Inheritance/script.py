import os
import random
import sys
import datetime
import builtins
#https://habrahabr.ru/post/137415/
class Employee:

    secret_value = 5

    def __init__(self, name, surname, patronymic, age, salary):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age
        self.salary = salary
    
    def fullName(self):
        return '{} {} {}, age {}, salary {}'.format(self.name, self.surname, self.patronymic, self.age, self.salary)

    def print_secret(self):
        return self.secret_value

class Developer(Employee): # inherit from eployee
    secret_value = 10

    def __init__(self, name, surname, patronymic, age, salary, language):
        super().__init__(name, surname, patronymic, age, salary) # calling base constructor
        #Employee.__init__(self, name, surname, patronymic, age) - same as above
        self.language = language

class Manager(Employee): # inherit from eployee

    def __init__(self, name, surname, patronymic, age, salary, developers = None):
        super().__init__(name, surname, patronymic, age, salary) # calling base constructor
        #Employee.__init__(self, name, surname, patronymic, age) - same as above
        if developers is None:
            self.developers = []
        else:
            self.developers = developers
    
    def add_developer(self, developer):
        if developer not in self.developers:
            self.developers.append(developer)
    
    def remove_developer(self, developer):
        if developer in self.developers:
            self.developers.remove(developer)
    
    def set_developer_salary(self, name, salary):
        for elem in self.developers:
            if elem.name == name:
                elem.salary = salary
                return


    def print_developers(self):
        for developer in self.developers:
            print('-->', developer.fullName())

#method resolution order - like in JS
#print(help(Developer))

#print(builtins.object) - Object

d1 = Developer('Vasya', 'Pupkin', 'Arkadievich', 35, 1111, 'python')
d2 = Developer('Petyr', 'Pupkin', 'Petkovich', 23, 22222, 'javascript')
d3 = Developer('A', 'B', 'C', 27, 12321322, 'c#')

m = Manager('Evgeny', 'Skyborev', 'Vladimirovich', 33, 33333, [d1, d2])

m.print_developers()

m.add_developer(d3)

m.set_developer_salary(d1.name, 2)
m.print_developers()

#isinstance() - instanceof js
#issubclass() -

print(isinstance(d1, Employee))
print(isinstance(m, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))