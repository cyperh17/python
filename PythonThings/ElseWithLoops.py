l = range(0, 10)

#for
for i in l:
    print(i, end=' ')
    if(i == 3):
        break #causes loop to break so then else not get called
else: #also called 'no break'. Else is called when break didnt called in the loop
    print('\nHit the for/else statetement!')

print('\n')

#while
i = 0
while i < (len(l) - 1):
    print(i, end=' ')
    i += 1
    if(i == 3):
        break #causes loop to break so then else not get called
else: #also called 'no break'. Else is called when break didnt called in the loop
    print('\nHit the for/else statetement!')

print('\n')
#example

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if(value == target):
            break
    else:
        return -1
    return i

l = ['a', 'b', 'c', 'd']
ind_one = find_index(l, 'd')
ind_two = find_index(l, 'ddd')

print(ind_one)
print(ind_two)