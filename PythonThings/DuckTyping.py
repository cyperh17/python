#if its quakcs then its a duck
#we dont care if its a Duck, we only care about is this object can quack

# class Duck:

#     def quack(self):
#         print('Duck, quacks')
    
#     def fly(self):
#         print('Duck, flys')

# class Person:

#     def quack(self):
#         print('Person, quacks')
    
#     def fly(self):
#         print('Person, flys')


#Duck typing
# def quack_and_fly(thing):
#     if isinstance(thing, Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print('Not a Duck')

#LBYL (Look Before You Leap) (Non-Pythonic way)
# def quack_and_fly(thing):
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()
    
#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()
    
#     print()

#EAFP (it's Easier to Ask Forgiveness than Permission) (Pythonic way)
# def quack_and_fly(thing):
#     try:
#         thing.quack()
#         thing.fly()
#     except AttributeError as ar:
#         print(ar)
    
#     print()

# d = Duck()
# p = Person()

# quack_and_fly(d)
# quack_and_fly(p)


################################################
# #person = { 'name': 'Jess', 'age': 23, 'job': 'Programmer' }
# person = { 'name': 'Jess', 'age': 23 }

# #LBYL
# # if 'name' in person and 'age' in person and 'job' in person:
# #     print('I am {name} and I am {age} years old. Working as a {job}.'.format(**person))
# # else:
# #     print('Some keys arent found')

# #EAFP
# try:
#     print('I am {name} and I am {age} years old. Working as a {job}.'.format(**person))
# except KeyError as k:
#     print('Missing {}'.format(k))

####################################################

#l = range(0, 10)

#LBYL
# if(len(l) > 6):
#     print(l[5])
# else:
#     print('Index does not exists')

#EAFP
# try:
#     print(l[11])
# except IndexError as i:
#     print(i)