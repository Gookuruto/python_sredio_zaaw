Oto 10 zadań dotyczących `dataclass` w Pythonie, wraz z przykładowymi rozwiązaniami:

1. Stwórz `dataclass` do reprezentacji informacji o książce zawierającej tytuł, autora i rok wydania.

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
```

2. Stwórz `dataclass` do przechowywania informacji o studencie, zawierającej imię, nazwisko, numer indeksu i oceny z kilku przedmiotów.

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    first_name: str
    last_name: str
    student_id: int
    grades: List[int]
```

3. Stwórz `dataclass` do przechowywania informacji o samochodzie, zawierającej markę, model, rok produkcji i liczbę przejechanych kilometrów.

```python
from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    mileage: float
```

4. Stwórz `dataclass` do reprezentacji informacji o filmie, zawierającej tytuł, reżysera, rok produkcji i ocenę.

```python
from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    director: str
    year: int
    rating: float
```

5. Stwórz `dataclass` do przechowywania informacji o produkcie w sklepie internetowym, zawierającej nazwę, cenę i dostępną liczbę sztuk.

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int
```

6. Stwórz `dataclass` do przechowywania informacji o zamówieniu online, zawierającej numer zamówienia, listę produktów i cenę całkowitą.

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    order_number: str
    products: List[Product]
    total_price: float
```

7. Stwórz `dataclass` do przechowywania informacji o użytkowniku aplikacji, zawierającej imię, nazwisko, adres email i wiek.

```python
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int
```

8. Stwórz `dataclass` do reprezentacji informacji o pacjencie w szpitalu, zawierającej imię, nazwisko, wiek i diagnozę.

```python
from dataclasses import dataclass

@dataclass
class Patient:
    first_name: str
    last_name: str
    age: int
    diagnosis: str
```

9. Stwórz `dataclass` do przechowywania informacji o restauracji, zawierającej nazwę, adres, ocenę i rodzaj kuchni.

```python
from dataclasses import dataclass

@dataclass
class Restaurant:
    name: str
    address: str
    rating: float
    cuisine: str
```

10. Stwórz `dataclass` do reprezentacji informacji o projekcie, zawierającej nazwę, opis, termin rozpoczęcia i termin zakończenia.

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Project:
    name: str
    description: str
    start_date: datetime
    end_date: datetime
```

Teraz możemy wykorzystać te `dataclass` do przechowywania i zarządzania różnymi rodzajami danych w naszych programach.