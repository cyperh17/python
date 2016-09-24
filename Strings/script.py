#Formating
###############
#convert to string - str()

#1
#person = { 'name': 'Jenn', 'age': 32 }

#sentence = 'My name is {name} and I am {age} yeard old.'.format(**person)
#sentence = 'My name is {} and I am {} yeard old.'.format(person.name, person.age) #same
#sentence = 'My name is {} and I am {} yeard old.'.format(person['name'], person['age']) #same

#2
# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text) #adding values by indexes in template

#3
#sentence = 'My name is {0[name]} and I am {0[age]} yeard old.'.format(person)

#4
# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Jack', 33)

# sentence = 'My name is {0.name} and I am {0.age} yeard old.'.format(p1)

#5
#l = ['Jann', 25]

#sentence = 'My name is {0[0]} and I am {0[1]} yeard old.'.format(l)
#sentence = 'My name is {0} and I am {1} yeard old.'.format(*l)

#6
#sentence = 'My name is {name} and I am {age} yeard old.'.format(name = 'Jann', age = 32)

#print(sentence)

#7
# for i in range(1, 11):
#     sentence = 'The value is {:03}'.format(i) #xxx number format
#     print(sentence)

#8
# pi = 3.1459265

# sentence = 'Pi is equals to {:.3f}'.format(pi)
# print(sentence)

#9
# sentence = '1 MB is eqaul to {:,} bytes'.format(1000**2) #comma separated value
# print(sentence)

# sentence = '1 MB is eqaul to {:,.2f} bytes'.format(1000**2) #combining
# print(sentence)


#10
#Dates
import datetime
d = datetime.datetime(2016, 9, 24, 12, 30, 45)

#print(d)

#sentence = '{:%B %d, %Y}'.format(d)
sentence = '{0:%B %d, %Y} feel on a {0:%A} and was the {0:%j} day of the year'.format(d)
print(sentence)