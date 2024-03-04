from examples.tlumaczenie_max_min_sort import sorted_custom, custom_max


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.age}"


lista = [Person("Adrian", "Nowak", 50),
         Person("Bartosz", "Kowalski", 25),
         Person("Cyprian", "Puchala", 28),
         Person("Dominika", "Lewandowska", 35),
         Person("Eustachy", "Omieljaniuk", 31),
         Person("Faustyna", "Stachowski", 100),
         Person("Gabriel", "Mistrz", 85),
         Person("Hermenegilda", "Gabka", 46),
         Person("Duriel", "Ancymon", 18)]

expected_value = [Person("Duriel", "Ancymon", 18),
                  Person("Bartosz", "Kowalski", 25),
                  Person("Cyprian", "Puchala", 28),
                  Person("Eustachy", "Omieljaniuk", 31),
                  Person("Dominika", "Lewandowska", 35),
                  Person("Hermenegilda", "Gabka", 46),
                  Person("Adrian", "Nowak", 50),
                  Person("Gabriel", "Mistrz", 85),
                  Person("Faustyna", "Stachowski", 95)
                  ]

# print(min(lista, key=lambda x: x.age))
# print(custom_max(lista, lambda x: x.age))

alfabetyczne_osoby = sorted(lista, key=lambda x: str(x.surname))
print(alfabetyczne_osoby)
# def sorted_multiple(*args, key=None):
#     lista = []
#     for i in args:
#         lista.append(sorted(i, key))
#     return tuple(lista)

# sorted_custom(lista, key=lambda x: x.age)
# sorted(lista, key=lambda x: str(x.surname))
#
# funkcja = lambda x: x.age
# last_element = lista[0]
# for i in lista[1:]:
#     print(funkcja(last_element))
#     print(funkcja(i))
# import pyuca
#
# coillector = pyuca.Collator()
# x = ["x", "z", "c","C","Z", "ć", "ą"]
#
# print(sorted(x,key=coillector.sort_key))

print(sorted(lista, key=lambda x: str(x.age)))
print(sorted(lista, key= lambda x: x.name[0]+x.surname[0]))