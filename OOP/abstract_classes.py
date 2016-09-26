#import abc
from abc import ABCMeta, abstractmethod

class BaseClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def printHam(self):
        pass

class DerivedClass(BaseClass):

    def printHam(self):
        print('Ham')

#x = BaseClass()

d = DerivedClass()
d.printHam()