def check_age():
    try:
        age = int(input("Podaj swój wiek: "))
        if age < 0:
            print("Wiek nie może być ujemny.")
        else:
            print("Twój wiek to:", age)
    except ValueError:
        print("Wprowadzona wartość nie jest liczbą całkowitą.")

check_age()
