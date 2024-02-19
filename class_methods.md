Oczywiście! Oto kilka przykładów metod klasowych w Pythonie:

1. Metoda klasowa do parsowania daty z tekstu:

```python
from datetime import datetime

class DateParser:
    DATE_FORMAT = "%Y-%m-%d"

    @classmethod
    def parse_date(cls, date_string):
        return datetime.strptime(date_string, cls.DATE_FORMAT).date()

# Przykład użycia
date_string = "2023-12-31"
parsed_date = DateParser.parse_date(date_string)
print(parsed_date)  # Output: 2023-12-31
```

2. Metoda klasowa do tworzenia obiektu na podstawie danych z pliku:

```python
class DataProcessor:
    @classmethod
    def process_file(cls, filename):
        with open(filename, 'r') as file:
            data = file.read()
            # Procesowanie danych i tworzenie obiektu
            return cls.create_from_data(data)

    @classmethod
    def create_from_data(cls, data):
        # Tworzenie obiektu na podstawie danych
        pass

# Przykład użycia
filename = "data.txt"
object_from_file = DataProcessor.process_file(filename)
```

3. Metoda klasowa do konwersji różnych jednostek miar:

```python
class Converter:
    @classmethod
    def feet_to_meters(cls, feet):
        return feet * 0.3048

    @classmethod
    def meters_to_feet(cls, meters):
        return meters / 0.3048

# Przykład użycia
feet_value = 10
meters_value = Converter.feet_to_meters(feet_value)
print(meters_value)  # Output: 3.048
```

4. Metoda klasowa do generowania unikalnych identyfikatorów:

```python
import uuid

class UniqueIDGenerator:
    @classmethod
    def generate_unique_id(cls):
        return str(uuid.uuid4())

# Przykład użycia
unique_id = UniqueIDGenerator.generate_unique_id()
print(unique_id)
```

Metody klasowe są przydatne do operacji związanych z klasą jako całością lub operacjami, które nie wymagają dostępu do instancji klasy. Można je wykorzystać do wykonywania różnych zadań w obrębie klasy, takich jak parsowanie danych, przetwarzanie plików czy konwersje jednostek miar.