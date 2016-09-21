import os
import random
import sys
import datetime

class Employee:

    def __init__(self, first, last): #dunder init
        self.first = first
        self.last = last
    
    @property
    def fullName(self):
        return "{} {}".format(self.first, self.last)
    
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullName.deleter # when we run del
    def fullName(self):
        print('Delete Name')
        self.first = None
        self.last = None
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

e1 = Employee('Vasya', 'Pupkin')

e1.fullName = 'Petya Petrov'

print(e1.fullName)
print(e1.email)

del e1.fullName
print(e1.fullName)