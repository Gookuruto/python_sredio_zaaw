def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Przed funkcja dekorowana")
        func(*args, **kwargs)
        print("po funkcji dekorowanej")

    return wrapper


def simple_decorator_with_args(argument_1, argument_2):
    def dec(func):
        def wrapper(*args, **kwargs):
            print(f"argument 1: {argument_1}")
            func(*args, **kwargs)
            print(f"argument 2: {argument_2}")

        return wrapper

    return dec


@simple_decorator
def hello():
    print("Hello")


# hello()

@simple_decorator_with_args("First", "second")
def hello_two(a, b):
    print(f"from hello two sum : {a + b}")


import time

print(time.time_ns())


def get_running_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print(f"{stop_time - start_time}")
        return result

    return wrapper


@get_running_time
def running_operation():
    return [i for i in range(10000000)]


@get_running_time
def running_in_loop():
    lista = []
    for i in range(10000000):
        lista.append(i)
    return lista


running_operation()

running_in_loop()


def funkcja_x():
    print("funckaj x")


def funkcja_y():
    print("funckaj y")


slownik = {
    "x": funkcja_x,
    "y": funkcja_y
}

slownik["x"]()
