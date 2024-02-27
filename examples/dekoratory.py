def log(func):
    """Dekorator logujący, który wyświetla nazwę funkcji oraz jej argumenty przy każdym wywołaniu."""
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(x, y):
    """Funkcja dodająca dwie liczby."""
    return x + y

print(add(3, 5))
