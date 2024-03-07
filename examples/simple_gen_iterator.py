class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration


# Użycie iteratora
iterator = SimpleIterator(5)
for item in iterator:
    print(item, end=" ")  # Output: 0 1 2 3 4

print("\n")


def simple_generator(limit):
    current = 0  # initialize początkowa (iterator __init__)
    while current < limit:  # warunek stopu generatora (iterator if contidion: else: raise StopIteration# )
        yield current  # wartości wyrzucana na zewnątrz to co zwracamy w next()(iterator return w metodzie __next__())
        current += 1  # logika dla kolejnego elementu


# Użycie generatora
generator = simple_generator(5)
for item in generator:
    print(item, end=" ")  # Output: 0 1 2 3 4
