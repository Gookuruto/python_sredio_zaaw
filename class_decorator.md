Oto przykład dekoratora klasowego w Pythonie:

```python
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function execution")
        result = self.func(*args, **kwargs)
        print("After function execution")
        return result

@DecoratorClass
def example_function():
    print("Function execution")

example_function()
```

W tym przykładzie `DecoratorClass` jest dekoratorem klasowym. Klasa ta przyjmuje funkcję jako argument w swoim konstruktorze i przechowuje ją w atrybucie `self.func`. Metoda `__call__` klasy `DecoratorClass` jest wywoływana, gdy obiekt tej klasy jest wywoływany jako funkcja. W naszym przypadku `DecoratorClass` jest używany jako dekorator dla funkcji `example_function`.

Gdy funkcja `example_function` jest wywoływana, dekorator klasowy wykonuje kod zdefiniowany przed i po wykonaniu funkcji. W naszym przypadku wydrukuje "Before function execution" przed wywołaniem funkcji i "After function execution" po wykonaniu funkcji.