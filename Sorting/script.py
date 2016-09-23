from operator import attrgetter

#sorted working with any enumerable
#.sort if for specific data type (e.g. list)
#li = [9,1,8,2,7,3,6,4,5]

#####################

#s_li = sorted(li) #creates new sorted list, asceing order of sorting
#s_li = sorted(li, reverse=True) #descending order of sorting
#print(s_li)

#####################

#li.sort() #sorting current list
#li.sort(reverse=True) #sorting current list, descending order
#print(li)

#####################

# tup = (9,1,8,2,7,3,6,4,5)
# s_tup = sorted(tup) #sorting tuple

# print(s_tup)

# di = { 'name': 'Corey', 'job': 'Programmer', 'age': None, 'os': 'Max' }
# s_di = sorted(di) #sorting dictionary (sorting by keys)

# print(s_di)

#####################

# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li, key=lambda x: abs(x)) #sorting with use of custom fuction
# print(s_li)

#####################

class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return ('{name} {age}, ${salary}'.format(**self.__dict__))

e1 = Employee('Vasya', 32, 70000)
e2 = Employee('Perya', 43, 80000)
e3 = Employee('Kolya', 56, 90000)
# print('{name} {age}, ${salary}'.format(**e1.__dict__))

employees = [e1, e2, e3]

s_employees = sorted(employees, key=lambda emp: emp.salary, reverse=True)
# s_employees = sorted(employees, key=attrgetter('age')) #same as above

print(s_employees)