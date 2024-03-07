import timeit

# Funkcja do profilowania
def some_function():
    result = 0
    for i in range(1000000):
        result += i
    return result

# Profilowanie funkcji z użyciem timeit
time = timeit.timeit("some_function()", setup="from __main__ import some_function", number=10)
print("Czas wykonania funkcji:", time)
