Oczywiście! Oto kilka przykładów użycia metod statycznych w Pythonie:

1. Metoda statyczna do obliczania wieku na podstawie daty urodzenia:

```python
from datetime import datetime

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    @staticmethod
    def calculate_age(birthdate):
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

# Użycie:
birthdate = datetime(1990, 5, 15)
john = Person("John", birthdate)
john_age = Person.calculate_age(birthdate)
print(f"{john.name} ma {john_age} lat.")
```

2. Metoda statyczna do walidacji numeru PESEL:

```python
class PeselValidator:
    @staticmethod
    def is_valid_pesel(pesel):
        if len(pesel) != 11:
            return False
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
        checksum = (10 - (checksum % 10)) % 10
        return checksum == int(pesel[-1])

# Użycie:
pesel_number = "12345678901"
is_valid = PeselValidator.is_valid_pesel(pesel_number)
print(f"Czy numer PESEL {pesel_number} jest poprawny? {is_valid}")
```

3. Metoda statyczna do generowania losowego hasła:

```python
import random
import string

class PasswordGenerator:
    @staticmethod
    def generate_password(length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

# Użycie:
random_password = PasswordGenerator.generate_password()
print(f"Losowe hasło: {random_password}")
```

Metody statyczne są użyteczne, gdy operacja nie wymaga dostępu do instancji klasy ani do jej atrybutów. Pozwalają one grupować funkcjonalność w obrębie klasy, co sprawia, że kod jest bardziej zorganizowany i czytelny.