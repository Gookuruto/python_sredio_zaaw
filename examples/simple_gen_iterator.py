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
    current = 0
    while current < limit:
        yield current
        current += 1

# Użycie generatora
generator = simple_generator(5)
for item in generator:
    print(item, end=" ")  # Output: 0 1 2 3 4
