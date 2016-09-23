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

print(sentence)

#https://youtu.be/vTX3IwquFkc?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=455