import copy


class A:
    def __init__(self, a, b, lista):
        self.a = a
        self.b = b
        self.lista = lista

    def __str__(self):
        return f"a: {self.a} b: {self.b} lista: {self.lista}"


a = A(1, 2, [1, 2, ['a', {'a': []}]])
b = copy.deepcopy(a)
try:
    a.lista.append(10)
    a.lista.clear()
    print(a)
    print(b)
    raise ValueError()
except ValueError:
    a = b
print(a)
print(b)
