import pytest
from metody_statyczne_i_klasowe import Calculator, DateHelper, StringHelper, Employee, MathHelper, FileHelper, \
    TemperatureConverter, URLHelper, StringFormatter, DatabaseHelper


# Testy dla klasy Calculator
def test_calculator_add():
    assert Calculator.add(5, 3) == 8


# Testy dla klasy DateHelper
def test_date_helper_is_leap_year():
    assert DateHelper.is_leap_year(2024) is True
    assert DateHelper.is_leap_year(2021) is False


# Testy dla klasy StringHelper
def test_string_helper_reverse():
    assert StringHelper.reverse("hello world") == "dlrow olleh"


# Testy dla klasy Employee
def test_employee_raise_salary():
    employees = [Employee("John", 50000), Employee("Alice", 60000)]
    Employee.raise_salary(employees)
    assert round(employees[0].salary, 3) == 55000
    assert round(employees[1].salary, 3) == 66000


# Testy dla klasy MathHelper
def test_math_helper_is_prime():
    assert MathHelper.is_prime(17) is True
    assert MathHelper.is_prime(10) is False


# Testy dla klasy FileHelper
def test_file_helper_count_lines(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as file:
        file.write("Line 1\nLine 2\nLine 3")
    assert FileHelper.count_lines(file_path) == 3


# Testy dla klasy TemperatureConverter
def test_temperature_converter_celsius_to_fahrenheit():
    assert TemperatureConverter.celsius_to_fahrenheit(30) == 86


# Testy dla klasy URLHelper
def test_url_helper_parse_url():
    url = "https://www.example.com/path/to/page?param1=value1&param2=value2#fragment"
    parsed_url = URLHelper.parse_url(url)
    assert parsed_url == ('https', 'www.example.com', '/path/to/page', '', 'param1=value1&param2=value2', 'fragment')


# Testy dla klasy StringFormatter
def test_string_formatter_remove_punctuation():
    text_with_punctuation = "Hello, world! How are you?"
    assert StringFormatter.remove_punctuation(text_with_punctuation) == "Hello world How are you"


# Testy dla klasy DatabaseHelper
def test_database_helper_execute_query():
    assert DatabaseHelper.execute_query("SELECT * FROM table") == "Result from database"
