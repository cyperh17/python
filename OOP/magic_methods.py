#http://mahugh.com/2016/04/27/python-and-vs-code/
#https://code.visualstudio.com/docs/editor/tasks
import os
import random
import sys
import datetime

#Special (Magic) methods
#double underscore - dunder

#__repr__(self) - debug representation of an object (used for degging and logging, also for recreating the object)
#__str__(self) - string representation of an object

class Employee:

    def __init__(self, first, last, pay, email): #dunder init
        self.first = first
        self.last = last
        self.pay = pay
        self.email = email
    
    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self): #dunder repr
        return "Employee('{}', '{}', '{}', '{}')".format(self.first, self.last, self.pay, self.email)
    
    def __str__(self): #dunder str
        return '{} - {}'.format(self.fullName(), self.email)

    def __add__(self, other): #overriding + operator for Employee
        return self.pay + other.pay
    
    def __len__(self): #overriding len method
        return len(self.fullName())
    
    @property #defining property
    def Email(self):
        return self.email

e1 = Employee('Vasya', 'Pupkin', 123, 'aaa@ya1.ru')
e2 = Employee('Petya', 'Petrovkin', 321, 'bbb@ya2.ru')


# print(e1 + e2)
# print(len(e1))

# print(e1)
# print(repr(e1))
# print(str(e1))

#Magic methods of base types
#print(int.__add__(1, 2))
#print(str.__add__('1', '2'))

#print(repr(datetime.date(2016, 9, 21)))