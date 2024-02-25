Przykładem dekoratora nakładanego na klasę może być dekorator, który dodaje dodatkowe funkcjonalności lub modyfikuje zachowanie metod w klasie. Poniżej znajdziesz przykład takiego dekoratora:

```python
def add_methods(cls):
    class NewClass(cls):
        def new_method(self):
            print("This is a new method added by the decorator")

    return NewClass

@add_methods
class MyClass:
    def existing_method(self):
        print("This is an existing method")

# Użycie klasy z dodaną nową metodą przez dekorator
obj = MyClass()
obj.existing_method()
obj.new_method()
```

W tym przykładzie dekorator `add_methods` przyjmuje klasę `cls` jako argument i zwraca nową klasę `NewClass`, która dziedziczy po klasie `cls`. Wewnątrz `NewClass` definiujemy nowe metody, które chcemy dodać do klasy. Po zastosowaniu dekoratora `add_methods` do klasy `MyClass`, obiekt klasy `MyClass` będzie miał dostęp do nowej metody `new_method`.