class Fibonacci:
    def __init__(self,limit):
        self.first = 0
        self.second = 1
        self.iteration = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration >= self.limit:
            raise StopIteration
        if self.iteration == 0:
            self.iteration += 1
            return self.first
        else:
            result = self.first + self.second
            self.first, self.second = self.second, result
            self.iteration += 1
            return result


fib = Fibonacci(20)

for i in fib:
    print(i)

'''
if n ==0: 0
if n ==1: 1
else = n_0 + n_1
'''
