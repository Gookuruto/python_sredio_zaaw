def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))  # Klucz zależy od argumentów
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper


# Przykład użycia:
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Oblicza wartość dla 10 i zapamiętuje wyniki dla kolejnych wartości
print(fibonacci(10))  # Zwraca wynik z pamięci podręcznej
