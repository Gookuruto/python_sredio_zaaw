def check_types(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Expected {arg_type} for argument {arg}, but got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Przykład użycia:
@check_types(int, str)
def example_function(num, text):
    print(f"Received integer: {num} and string: {text}")

example_function(10, "Hello")    # Powinno się wykonać bez problemu
example_function("test", 10)     # Powinno wywołać wyjątek TypeError
