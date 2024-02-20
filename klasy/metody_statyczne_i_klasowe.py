# 1
class Calculator:
    @classmethod
    def add(cls, a, b):
        return a + b


# Przykład użycia
result = Calculator.add(5, 3)
print(result)  # Output: 8


# 2

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


# 3
class StringHelper:
    @staticmethod
    def reverse(string):
        return string[::-1]


# Przykład użycia
text = "hello world"
print(StringHelper.reverse(text))  # Output: "dlrow olleh"


# 4


# Przykład użycia
class Employee:
    salary_increase_percentage = 10  # Procent podwyżki pensji dla wszystkich pracowników

    @classmethod
    def raise_salary(cls, employees):
        for employee in employees:
            employee.salary *= (1 + cls.salary_increase_percentage / 100)

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = [Employee("John", 50000), Employee("Alice", 60000)]
Employee.raise_salary(employees)
for employee in employees:
    print(f"{employee.name}: {employee.salary}")  # Output: Pensje po podwyżce


# 5

class MathHelper:
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


# Przykład użycia
number = 17
print(MathHelper.is_prime(number))  # Output: True


# 6
class FileHelper:
    @classmethod
    def count_lines(cls, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return len(lines)


# Przykład użycia
filename = "example.txt"
print(FileHelper.count_lines(filename))  # Output: Liczba wierszy w pliku


# 7
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


# Przykład użycia
celsius_temp = 30
print(
    TemperatureConverter.celsius_to_fahrenheit(celsius_temp))  # Output: Odpowiednia temperatura w stopniach Fahrenheita
# 8
from urllib.parse import urlparse


class URLHelper:
    @staticmethod
    def parse_url(url):
        parsed_url = urlparse(url)
        return parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment


# Przykład użycia
url = "https://www.example.com/path/to/page?param1=value1&param2=value2#fragment"
print(URLHelper.parse_url(url))  # Output: Tuple zawierający różne części adresu UR
# 9
import string


class StringFormatter:
    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))


# Przykład użycia
text_with_punctuation = "Hello, world! How are you?"
print(StringFormatter.remove_punctuation(text_with_punctuation))  # Output: "Hello world How are you"


# 10

class DatabaseHelper:
    @classmethod
    def execute_query(cls, query):
        # Wykonaj zapytanie do bazy danych
        return "Result from database"


# Przykład użycia
query = "SELECT * FROM table"
print(DatabaseHelper.execute_query(query))  # Output: Wynik zapytania do bazy danych
