import time

# Dekorator do pomiaru czasu wykonania funkcji
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

# Dekorator do logowania
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Dekorator do memoizacji
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Przykładowa funkcja do testów
@measure_time
@log_call
@memoize
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Testy
def test_measure_time():
    @measure_time
    def test_func():
        time.sleep(0.1)
    start_time = time.time()
    test_func()
    end_time = time.time()
    assert (end_time - start_time) >= 0.1

def test_log_call(capsys):
    @log_call
    def test_func(a, b):
        pass
    test_func(1, 2)
    captured = capsys.readouterr()
    assert "Calling function test_func with args: (1, 2), kwargs: {}\n" in captured.out

def test_memoize():
    @memoize
    def test_func(a):
        return a + 1
    assert test_func(1) == 2
    assert test_func(1) == 2

if __name__ == "__main__":
    test_measure_time()
    test_log_call()
    test_memoize()
    print("All tests passed!")
