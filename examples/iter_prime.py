from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.gen_number = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.gen_number >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.gen_number += 1
            return self.number
        return self.__next__()


iterator = PrimeIterator(20)

lista = [prime for prime in iterator]


# print(lista)


# for item in iterator:
#     print(item)


def prime_generator(n):
    num = 2
    gen_number = 0
    while gen_number < n:
        if is_prime(num):
            yield num
            gen_number += 1
        num += 1


# gen = prime_generator(20)
#
# for i in gen:
#     print(i)


class MyIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop(0)


class UdajeIterator:
    def __init__(self, data):
        self.data = data
        self.iterator = MyIterator(data)

    def __iter__(self):
        return self.iterator


ui = UdajeIterator([10, 1, 5, 6, 7, 9, 8, 2])
iterator = MyIterator([10, 1, 5, 6, 7, 9, 8, 2])
for i in ui:
    print(i, end=" ")

print()
for i in iterator:
    print(i, end=" ")
