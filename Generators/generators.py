#Fibonacci

def Fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        yield '{}: {}'.format(i + 1, a)
        a, b = b, a + b

for item in Fibonacci(10):
    print(item)