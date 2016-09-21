#http://www.tutorialspoint.com/python/python_variable_types.htm

import os
import random
import sys

def print_list(*lst):
    print(lst)

def print_dict(**dic):
    print(dic)

print_list(1,2,3)
print_dict(name='vasya', age=1)