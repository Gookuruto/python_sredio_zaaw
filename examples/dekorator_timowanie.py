import time

def timer(func):
    """Dekorator mierzący czas wykonania funkcji."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@timer
def slow_function():
    """Funkcja, która wykonuje się wolno."""
    time.sleep(2)
    return "Function executed"

print(slow_function())
