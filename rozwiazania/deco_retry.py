import time

def retry_on_error(max_retries, delay=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    retries += 1
                    time.sleep(delay)
            raise RuntimeError(f"Function {func.__name__} failed after {max_retries} retries")
        return wrapper
    return decorator

# Przykład użycia:
@retry_on_error(max_retries=3, delay=1)
def example_function():
    import random
    if random.random() < 0.5:
        raise ValueError("Random error")
    else:
        return "Success"

#print(example_function())  # Może spróbować ponownie wywołać funkcję w przypadku błędu


def loop_function():
    for i in range(10):
        yield i

generator = loop_function()

for i in generator:
    print(i)