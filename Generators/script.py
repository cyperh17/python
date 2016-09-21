#l = (x*x for x in range(0, 10))
def get_num():
    for n in range(0, 10):
        yield n

for n in get_num():
    print(n)