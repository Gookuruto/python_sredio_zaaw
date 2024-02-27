from abstraction.car_interface import Car


class ElectricCar(Car):

    def __init__(self):
        self.charging_time = 120
        self.power = 200

    def start_breaking(self):
        print("EV Car breaking")

    def drive(self):
        print("EV Car driving")


def calculate():
    print("calulate ev cos.")
