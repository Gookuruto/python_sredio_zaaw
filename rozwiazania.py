class ValueTooSmallError(Exception):
    pass

def handle_type_conversion_error():
    try:
        user_input = input("Podaj liczbę całkowitą: ")
        number = int(user_input)
        print("Wprowadzona liczba to:", number)
    except ValueError:
        print("Podana wartość nie jest liczbą całkowitą.")

def handle_zero_division_error():
    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        result = num1 / num2
        print("Wynik dzielenia:", result)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")

def check_value(number):
    if number < 5:
        raise ValueTooSmallError("Podana wartość jest zbyt mała.")

def handle_custom_exception():
    try:
        user_input = int(input("Podaj liczbę: "))
        check_value(user_input)
        print("Podana liczba jest wystarczająco duża.")
    except ValueTooSmallError as e:
        print(e)

def handle_file_reading():
    try:
        with open("plik.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Nie można odnaleźć pliku.")
    except PermissionError:
        print("Brak uprawnień do odczytu pliku.")

def handle_multiple_exceptions():
    try:
        filename = input("Podaj nazwę pliku: ")
        with open(filename, "r") as file:
            content = file.read()
            print("Zawartość pliku:")
            print(content)
    except FileNotFoundError:
        print("Plik o podanej nazwie nie istnieje.")
    except PermissionError:
        print("Brak uprawnień do odczytu pliku.")
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", e)

def handle_index_error():
    try:
        my_list = [1, 2, 3]
        index = int(input("Podaj indeks elementu do wyświetlenia: "))
        print("Wybrany element to:", my_list[index])
    except IndexError:
        print("Podany indeks jest poza zakresem listy.")

def handle_key_error():
    try:
        my_dict = {"a": 1, "b": 2, "c": 3}
        key = input("Podaj klucz do znalezienia wartości: ")
        print("Wartość dla klucza {} to: {}".format(key, my_dict[key]))
    except KeyError:
        print("Podany klucz nie istnieje w słowniku.")

def handle_attribute_error():
    try:
        my_str = "Hello, world!"
        print(my_str.nonexistent_method())
    except AttributeError:
        print("Podany obiekt nie posiada tej metody.")

if __name__ == "__main__":
    handle_type_conversion_error()
    handle_zero_division_error()
    handle_custom_exception()
    handle_file_reading()
    handle_multiple_exceptions()
    handle_index_error()
    handle_key_error()
    handle_attribute_error()
