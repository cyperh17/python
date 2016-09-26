import time
import threading

arr = [2,3,8,9]

def calc_square(numbers):
    print('Calculating square of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('Square of {} is {}'.format(n, n*n))

def calc_cube(numbers):
    print('Calculating cube of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('Cube of {} is {}'.format(n, n*n*n))

def NonThreading():
    t = time.time()

    calc_square(arr)
    calc_cube(arr)

    print('Done in {}'.format(time.time() - t))

def UsingThreading():
    t = time.time()
    
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Done in {}'.format(time.time() - t))

#################
#Main
###################

#NonThreading()
UsingThreading()