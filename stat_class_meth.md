Oto 10 zadań z przykładowymi rozwiązaniami dotyczących metod klasowych i statycznych w Pythonie:

1. Stwórz klasę `Calculator` z metodą klasową `add`, która przyjmuje dwa argumenty i zwraca ich sumę.

```python
class Calculator:
    @classmethod
    def add(cls, a, b):
        return a + b

# Przykład użycia
result = Calculator.add(5, 3)
print(result)  # Output: 8
```

2. Stwórz klasę `DateHelper` z metodą statyczną `is_leap_year`, która przyjmuje rok jako argument i zwraca `True`, jeśli rok jest rokiem przestępnym, a w przeciwnym razie `False`.

```python
class DateHelper:
    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False

# Przykład użycia
leap_year = 2024
print(DateHelper.is_leap_year(leap_year))  # Output: True
```

3. Stwórz klasę `StringHelper` z metodą statyczną `reverse`, która przyjmuje ciąg znaków i zwraca jego odwróconą wersję.

```python
class StringHelper:
    @staticmethod
    def reverse(string):
        return string[::-1]

# Przykład użycia
text = "hello world"
print(StringHelper.reverse(text))  # Output: "dlrow olleh"
```

4. Stwórz klasę `Employee` z metodą klasową `raise_salary`, która zwiększa pensję wszystkich pracowników o określony procent.

```python
class Employee:
    salary_increase_percentage = 10  # Procent podwyżki pensji dla wszystkich pracowników

    @classmethod
    def raise_salary(cls, employees):
        for employee in employees:
            employee.salary *= (1 + cls.salary_increase_percentage / 100)

# Przykład użycia
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [Employee("John", 50000), Employee("Alice", 60000)]
Employee.raise_salary(employees)
for employee in employees:
    print(f"{employee.name}: {employee.salary}")  # Output: Pensje po podwyżce
```

5. Stwórz klasę `MathHelper` z metodą statyczną `is_prime`, która przyjmuje liczbę całkowitą jako argument i zwraca `True`, jeśli liczba jest liczbą pierwszą, a w przeciwnym razie `False`.

```python
class MathHelper:
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

# Przykład użycia
number = 17
print(MathHelper.is_prime(number))  # Output: True
```

6. Stwórz klasę `FileHelper` z metodą klasową `count_lines`, która liczy liczbę wierszy w pliku tekstowym.

```python
class FileHelper:
    @classmethod
    def count_lines(cls, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return len(lines)

# Przykład użycia
filename = "example.txt"
print(FileHelper.count_lines(filename))  # Output: Liczba wierszy w pliku
```

7. Stwórz klasę `TemperatureConverter` z metodą statyczną `celsius_to_fahrenheit`, która konwertuje stopnie Celsiusza na stopnie Fahrenheita.

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# Przykład użycia
celsius_temp = 30
print(TemperatureConverter.celsius_to_fahrenheit(celsius_temp))  # Output: Odpowiednia temperatura w stopniach Fahrenheita
```

8. Stwórz klasę `URLHelper` z metodą statyczną `parse_url`, która przyjmuje adres URL jako argument i zwraca części adresu URL (np. protokół, domenę, ścieżkę, parametry).

```python
from urllib.parse import urlparse

class URLHelper:
    @staticmethod
    def parse_url(url):
        parsed_url = urlparse(url)
        return parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment

# Przykład użycia
url = "https://www.example.com/path/to/page?param1=value1&param2=value2#fragment"
print(URLHelper.parse_url(url))  # Output: Tuple zawierający różne części adresu URL
```

9. Stwórz klasę `StringFormatter` z metodą statyczną `remove_punctuation`, która usuwa znaki interpunkcyjne z ciągu znaków.

```python
import string

class StringFormatter:
    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

# Przykład użycia
text_with_punctuation = "Hello, world! How are you?"
print(StringFormatter.remove_punctuation(text_with_punctuation))  # Output: "Hello world How are you"
```

10. Stwórz klasę `DatabaseHelper` z metodą klasową `execute_query`, która wykonuje zapytanie do bazy danych i zwraca wynik.

```python
class DatabaseHelper:
    @classmethod
    def execute_query(cls, query):
        # Wykonaj zapytanie do bazy danych
        return "Result from database"

# Przykład użycia
query = "SELECT * FROM table"
print(DatabaseHelper.execute_query(query))  # Output: Wynik zapytania do bazy danych
```

Zadania te demonstrują różne sposoby użycia metod klasowych i statycznych w Pythonie. Można je dostosować do swoich potrze

b lub wykorzystać jako punkt wyjścia do tworzenia bardziej zaawansowanych zadań.