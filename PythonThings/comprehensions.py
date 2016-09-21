# give back each number in a list squared

squares = [num*num for num in range(0, 11)]
squares2 = map(lambda n: n ** 2, range(0, 11))

print(squares)

for n in squares2:
    print(n, end=' ')