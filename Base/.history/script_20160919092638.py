import random
import sys
import os

#Loops
#for
'''
for x in range(0, 10) :  # prints numbers from 0 to 9 in one line (no breaks)
    print(x, ' ', end="")

print('\n') # newline

r_list = [1,2,3,4,5,6,7,8,9,10]

print('\n') # newline

for y in r_list : # prints the list
    print(y)

print('\n') # newline

for y in [1,2,3,4,5,6,7,8,9,10] : # prints created in loop list
    print(y)

print('\n') # newline

num_list = [[1,2,3], [4,5,6]]

print('\n') # newline
print('num_list: ')
for x in num_list :
    print('[', '', end="")
    for y in x :
        print(y, ', ', end="")
    print(']', '', end="")
    print('\n')

print('\n') # newline
print('num_list: ')
for x in range(0, 3) :
    print('[', '', end="")
    for y in range(0, 3) :
        print(num_list[x][y], ', ', end="")
    print(']', '', end="")
    print('\n')
'''

#while
'''
random_num = random.randrange(0, 100) # random range

while(random_num != 15) :
    print(random_num)
    random_num = random.randrange(0, 100)

i = 0
while(i <= 20)
    if(i%2 == 0):
        print(i)
    else(i == 9):
        break
    else:
        i += 1  # i = i + 1
        continue

    i += 1
'''

#Functions
'''
def addNumber(fNumb, lNumb): # functoin must be defined before called
    sumNum = fNumb + lNumb # sumNum - local variable
    return sumNum

print(addNumber(1, 3))
'''

'''
print('what is your name')
name = sys.stdin.readline()

print('Hello', name)
'''

#Strings
'''
long_string = 'A very very long string of many many words inside'

print(long_string[0:10]) # prints indexes from 0 to 9
print(long_string[0:]) # prints every index from 0 to the end
print(long_string[-5:]) # prints 5 characters from end
print(long_string[:-5]) # prints every char from 0 to length - 5
print(long_string[:4]) # from 0 to 4 characters (substring)

print('%c is my character %s is a letter and my nubmer %d and other number %.5f' % 
('X', 'favorite', 1, .24132432423))

print(long_string.capitalize()) # capitalize

print(long_string.find('words')) # index of (case sensitive)

print(long_string.isalpha()) # is aplha only

print(long_string.isalnum()) # is numbers only

print(long_string.replace('words', 'wwwww')) # replace

print(long_string.strip()) # trim

quote_list = long_string.split(' ') # split by space
print(quote_list)
'''

#File IO

test_file = open('test.txt', 'wb')

print(test_file.mode) # mode whis is used to open current file
print(test_file.name) # file name
test_file.write(bytes('Write me to the file', 'UTF-8'))