try:
    raise ArithmeticError #raise an error
    f = open('t.txt')
    a = 1 # never executed
    print(a)
except ArithmeticError as ex:
    print('ArithmeticError: ', ex)
except FileNotFoundError as ex: #if exception happend
    print('FileNotFoundError: ', ex)
except Exception as ex: #if exception happend
    print('Generic Error: ', ex)
except Exception: #it is not required to have names for Exception
    print('Error!')
else: # if no errors/exceptions
#this else is usefull when in try we are trying to open file and in else we are reading file data
    print('In else')
finally: #executes always
    print('In finally')