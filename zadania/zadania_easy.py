'''
Wypisywanie kwadratow liczb z listy
'''

import threading


def print_squares(numbers):
    for i in numbers:
        print(f"Kwadrat: {i} = {i**2} ")


def main():
    numbers = [i for i in range(10000)]

    # Tworzymy wątek i uruchamiamy funkcję obliczającą sumę kwadratów


'''
Wypisywanie liczb parzystych i nieparzystych:
'''

import threading

def print_even_numbers():
    for i in range(0, 11, 2):
        print("Parzysta:", i)

def print_odd_numbers():
    for i in range(1, 11, 2):
        print("Nieparzysta:", i)

def main():
    # Tworzymy dwa wątki i uruchamiamy funkcje drukujące liczby parzyste i nieparzyste
