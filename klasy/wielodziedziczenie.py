# Zadanie 1: Klasy bazowe
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Animal sound")


class Machine:
    def __init__(self, model):
        self.model = model

    def start(self):
        print("Machine started")


# Zadanie 2: Klasa potomna
class Robot(Animal, Machine):
    def __init__(self, species, model):
        Animal.__init__(self, species)
        Machine.__init__(self, model)

    def action(self):
        print("Performing action")


# Zadanie 3: Metody konfliktowe
class Animal:
    def method(self):
        print("Animal method")


class Machine:
    def method(self):
        print("Machine method")


class Robot(Animal, Machine):
    pass


robot = Robot()
robot.method()  # Output: Animal method


# Zadanie 4: Wywoływanie metod z klas bazowych
class Robot(Animal, Machine):
    def perform_tasks(self):
        self.make_sound()  # Method from Animal class
        self.start()  # Method from Machine class


robot = Robot("Robot", "Model 1")
robot.perform_tasks()


# Output:
# Animal sound
# Machine started

# Zadanie 5: Atrybuty konfliktowe
class Animal:
    def __init__(self):
        self.name = "Animal"


class Machine:
    def __init__(self):
        self.name = "Machine"


class Robot(Animal, Machine):
    pass


robot = Robot()
print(robot.name)  # Output: Machine


# Zadanie 6: Przesłanianie metod
class Animal:
    def method(self):
        print("Method from Animal class")


class Machine:
    def method(self):
        print("Method from Machine class")


class Robot(Animal, Machine):
    def method(self):
        print("Method from Robot class")


robot = Robot()
robot.method()  # Output: Method from Robot class


# Zadanie 7: Zastosowanie super()
class Animal:
    def method(self):
        print("Method from Animal class")


class Machine:
    def method(self):
        print("Method from Machine class")


class Robot(Animal, Machine):
    def method(self):
        super().method()
        print("Method from Robot class")


robot = Robot()
robot.method()


# Output:
# Method from Animal class
# Method from Robot class

# Zadanie 8: Przeciążanie operatorów
class Animal:
    def __add__(self, other):
        print("Adding animals")


class Machine:
    def __add__(self, other):
        print("Adding machines")


class Robot(Animal, Machine):
    pass


robot = Robot()
robot + robot  # Output: Adding animals
