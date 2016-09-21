import threading
import time
import random

def executeThread(i):
    print('Thread {} sleeps at {}.'.format(
        i,
        time.strftime('%H:%M:%S', time.gmtime())
    ))

    randomSleepTime = random.randint(1, 5)

    time.sleep(randomSleepTime)

    print('Thread {} stops sleeping at {}'.format(
        i,
        time.strftime('%H:%M:%S', time.gmtime())
    ))

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print('Active Threads: ', threading.activeCount())

    print('Thread Objects: ', threading.enumerate())

#https://youtu.be/Bs7vPNbB9JM?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&t=442