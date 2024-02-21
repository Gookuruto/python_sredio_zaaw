def zadanie_1():
    value = input("Wprowadź liczbe całkowitą: ")
    try:
        value = int(value)
    except ValueError:
        print(f"wartość {value} nie jest liczba całkowitą")


def zadanie_2():
    a = float(input("Podaj liczbe a: "))
    b = float(input("Podaj liczbe b: "))
    try:
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("Nie dziel przez 0.")


class ValueTooSmallError(Exception):
    pass


def zadanie_3(value: int):
    if value <= 5:
        raise ValueTooSmallError()
    print("Liczba jest wystarczająco duża.")


def zadanie_4():
    try:
        with open('plik.txt', "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Nie można znaleźć pliku")
    except PermissionError:
        print("Brak uprawnień do odczytu pliku.")


def zadanie_5():
    filename = input("podaj nazwe pliku: ")
    if len(filename.split(".")) < 2:
        filename = f"{filename}.txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("Zawartość pliku:")
            print(content)
    except FileNotFoundError:
        print("Podany plik nie istnieje!")
    except PermissionError:
        print("Brak uprawnień do odczytu pliku.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd {e}")


class NegativeAgeValueError(Exception):
    pass


def zadanie_6():
    try:
        wiek = int(input('podaj swój wiek:'))
        if wiek < 0:
            raise NegativeAgeValueError()
    except ValueError:
        print("Wiek musi być liczbą całkowitą")
    except NegativeAgeValueError:
        print("Wiek nie moze być ujemny.")


def zadanie_7():
    lista = ["1", "2", "abc", 10, 12.3, "cc", "jajko"]
    for element in lista:
        try:
            converted_value = int(element)
        except ValueError as e:
            print(e)
            print(element)


class InvalidEmailError(Exception):
    def __init__(self, email):
        message = f"given email {email} is not valid"
        super().__init__(message)


def zadanie_8():
    email = input("podaj email:")
    if "@" not in email:
        raise InvalidEmailError(email)


def zadanie_9():
    while True:
        try:
            value = int(input("Podaj liczbe całkowitą: "))
        except ValueError:
            print("to nie jest poprawna liczba")
            continue
        else:
            break


def zadanie_10():
    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            result = "infinite"
        return result

    print(divide(10, 0))
