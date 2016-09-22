#if its quakcs then its a duck
#we dont care if its a Duck, we only care about is this object can quack
#https://youtu.be/x3v9zMX1s4s?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=286
class Duck:

    def quack(self):
        print('Duck, quacks')
    
    def fly(self):
        print('Duck, flys')

class Person:

    def quack(self):
        print('Person, quacks')
    
    def fly(self):
        print('Person, flys')


def quack_and_fly(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('Not a Duck')

d = Duck()
p = Person()

quack_and_fly(d)
quack_and_fly(p)