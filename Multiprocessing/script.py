import time
import multiprocessing

square_result = []
cube_result = []

def calc_square(numbers):
    #global square_result #telling to python that its a global variable

    for i in numbers:
        r = i*i
        square_result.append(r)
        print('square {}'.format(r))

def calc_cube(numbers):
    #global cube_result #telling to python that its a global variable

    for i in numbers:
        r = i*i*i
        square_result.append(r)
        print('cube {}'.format(r))

if __name__ == '__main__':
    arr = [2,3,8,9]

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Done in {}'.format(time.time() - t))