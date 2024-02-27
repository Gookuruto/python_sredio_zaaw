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
print(john.calculate_age(john.birthdate))
john_age = Person.calculate_age(birthdate)
print(f"{john.name} ma {john_age} lat.")