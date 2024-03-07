import cProfile

# Funkcja do profilowania
def some_function():
    result = 0
    for i in range(1000000):
        result += i
    return result

# Profilowanie funkcji z użyciem cProfile
cProfile.run("some_function()")
