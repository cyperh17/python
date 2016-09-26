# a = [1,2,3,4,5,6,7,8,9,10]

# a_iterator = iter(a)

# print(next(a_iterator))

# for item in itr:
#     print(item)


######################

class RemoteControl():
    def __init__(self):
        self.channels = ['1', '2', '3', '4']
        self.index = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if(self.index == len(self.channels)):
            raise StopIteration

        return self.channels[self.index]

r = RemoteControl()
r_iter = iter(r)

# print(next(r_iter))
# print(next(r_iter))
