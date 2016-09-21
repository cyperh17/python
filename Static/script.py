import os
import sys
import random
import datetime

class Person:
    len2 = 0
    __private_prop = 0

class Employee:
    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
    
    def toString(self):
        return '{} {} {}'.format(self.name, self.surname, self.pay)
    
    @classmethod
    def from_string(self, str):
        name, surname, pay = str.split('-')
        return Employee(name, surname, pay)

#print(Person.__dict__)

class EmployeesList:
    len2 = 2 #class property

    @classmethod #class method
    def set_raise(self, amount): #self current instance
        print(self.len)
        print(self.len2)
        print(amount)

EmployeesList.len = 1 #class Property

#print(EmployeesList.__dict__)

el = EmployeesList()
EmployeesList.set_raise(3)

[first, last, pay] = 'Vasya-Petya-111'.split('-') #destructing
first, last, pay = 'Vasya-Petya-111'.split('-') #destructing

#print(first, last, pay)

empl = Employee.from_string('Max-Maxin-1000')

#print(empl.toString())


#print(1 in [1,2,3])

class DateExtensions:
    @staticmethod # static method
    def is_workday(day): #static methods dont take self args
        return day.weekday() in [5,6] #5,6 sunday and saturday

d = datetime.date(2016, 9, 18)

#print(DateExtensions.is_workday(d))

