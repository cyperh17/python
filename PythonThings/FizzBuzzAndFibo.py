import functools

#Fizz Buzz

def FizzBuzz():
    for num in range(1, 101):
        if num%5 == 0 and num%3 == 0:
            print('FizzBuzz')
        elif num%5 == 0:
            print('Buzz')
        elif num%3 == 0:
            print('Fizz')
        else:
            print(num)

#Fibonacci
def Fibonacci():
    a, b = 0, 1
    for i in range(0, 10):
        print(a)
        a, b = b, a + b

def FibonacciRecursion(n):
    if(n < 2):
        return 0
    if(n == 2):
        return 1
    return FibonacciRecursion(n - 1) + FibonacciRecursion(n - 2)

print(FibonacciRecursion(10))