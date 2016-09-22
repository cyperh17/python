#comprehension - is an easiest and more readable way to create something (for inst. list)

# give back each number in a list squared

squares = [num*num for num in range(0, 11)]
squares2 = map(lambda n: n ** 2, range(0, 11))

# print(squares)

# for n in squares2:
#     print(n, end=' ')

nums = range(0, 11)

# l = []
# for n in nums:
#     l.append(n)
# print(l)


#list comprehensions
#l = [n for n in nums]
#print(l)

#l = [n*n for n in nums]
#print(l)

# l = map(lambda n: n*n, nums)
# print(l)

#l = [n for n in nums if n%2 == 0]
#print(l)

# l = filter(lambda n: n%2 == 0, nums)
# print(l)

# l = []
# for letter in 'abcd':
#     for num in range(4):
#         l.append((letter, num))
# print(l)

# l = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(l)

#dict comprehensions
#names = ['a', 'b', 'c']
#heroes = ['Batman', 'Superman', 'Spiderman', 'Deadpool']
#print(zip(names, heroes))

# l = {}
# for name, hero in zip(names, heroes):
#     l[name] = hero
# print(l)

# l = { name: hero for name, hero in zip(names, heroes) if name != 'a' }
# print(l)


#set comprehensions
#nums = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,7,8,8,9,9,9,9]

#s = set()
# for n in nums:
#     s.add(n)
# print(s)

# s = { n for n in nums }
# print(s)


#Generator Expressions

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# g = gen_func(nums)

# for i in g:
#     print(i, end=' ')


# g = (n*n for n in nums)

# for i in g:
#     print(i, end=' ')