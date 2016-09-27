# import random
# import sys
# import os

#print('Hello World!')

# Comment

'''
Multiline Comment
'''

#name = 'Dmitry' # a variable
#print(name)

#Data Types
#1. Numbers
#2. Strings
#3. Lists
#4. Tuples
#5. Dictionaries

#Operators
#+ - * / %
#** - exponent
#// - floor division => 14.5 becomes 14

#Printing
'''
print('5 + 2=', 5+2)
print('5 - 2=', 5-2)
print('5 * 2=', 5*2)
print('5 / 2=', 5/2)
print('5 % 2=', 5%2)
print('5 ** 2=', 5**2)
print('5 // 2=', 5//2)

#Priority
print('1 + 2 - 3 * 2 = ', 1 + 2 - 3 * 2)
print('(1 + 2 - 3) * 2 = ', (1 + 2 - 3) * 2)

quote = "\""


multi_line_quote = \''' just
like everyone else\'''

new_string = quote + multi_line_quote

print("%s %s %s" % ('asdadsa', quote, multi_line_quote))

print('\n' * 5)

print('i dont like ', end='')
print('newlines')
'''


#List
'''
g_list = ['asda', 'ff', 'sd']

print(g_list[0]) #print by index
print(g_list[0:4]) #print list items (0, 2) - не включительно

g_list_other = ['a', 'b', 'c']

g_list_new = [g_list_other, g_list] # list inside list

print(g_list_new[0:2]) # print list of lists
print(g_list_new[0][1]) # print first lists element at index 1

g_list_other.append('d') # adding new item to list
print(g_list_other[0:4])

g_list_other.insert(0, 'e') # inserting 'e' at 0 index
print(g_list_other[0:5])

g_list_other.remove('e') # removing item
print(g_list_other[0:5])

g_list_other.sort() # sorting
print(g_list_other[0:5])

g_list_other.reverse() # reversing
print(g_list_other[0:5])

del g_list_other[0] # deleting item at index 0
print(g_list_other[0:5])

l = g_list_other + g_list # concating lists
print(l[0:10])

print(len(l)) # list length
print(max(l)) # max value from l
print(min(l)) # min value from l
'''


##Tuples
#Tuple cannot be changed aftes it has been created
'''
pi_tuple = (3,1,4,1,5,9) # creating tuple

print(pi_tuple)

new_list = list(pi_tuple) # converting tuple to list
print(new_list)

new_tuple = tuple(new_list) # converting list to tuple
print(new_tuple)

len(pi_tuple)
min(pi_tuple)
max(pi_tuple)
'''


#Dictionary
#Can not be joined with +
'''
super_villans = { 'key': 'value', 'Fiddler': 'Isaac Bowin' }
print(super_villans)

print(super_villans['key']) # find value by key

del super_villans['key'] # del by key

print(super_villans)

super_villans['Fiddler'] = 0 # change the value by key

print(super_villans)
print(len(super_villans)) # prints the length of dictionary
print(super_villans.get('Fiddler')) # gets value
print(super_villans.keys()) # print list of all keys
print(super_villans.values()) # print list of all values

'''

#Conditions
'''
if
else
elif
==
!=
>
<
>=
<=
'''

'''
age = 21

if age > 16 :
    print('older than 16')
else :
    print('greater than 16')

if age >= 21 :
    print('>= 21')
elif age <= 21 :
    print('<= 21')
else : print('else')
'''

#Logical OP
'''
and
or
not
'''

'''
if ((age >= 1) and (age <= 21)) :
    print('>= 21')
elif (age == 21) or (age >= 65)
    print('Great')
elif not(age == 21)
    print('Great 2')
else : print('yeah')
'''

#Loops
# https://youtu.be/N4mEzFDjqtA?t=1184


class Human():
    name = None
    age = None
    
    def __init__(self, name, age):
        Human.name = name
        Human.age = age

    def __str__(self):
        return '{} {}'.format(Human.name, Human.age)

h = Human(name='Vasya', age=32)

print(h)