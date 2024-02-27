from datetime import datetime

class DateParser:
    DATE_FORMAT = "%Y-%m-%d"

    @classmethod
    def parse_date(cls, date_string):
        return datetime.strptime(date_string, cls.DATE_FORMAT).date()

# Przykład użycia
date_string = "2023-12-31"
parsed_date = DateParser.parse_date(date_string)
print(type(parsed_date))
print(parsed_date)  # Output: 2023-12-31