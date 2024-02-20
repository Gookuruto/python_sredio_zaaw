1. Obsługa błędów przy konwersji typów:

Poproś użytkownika o wprowadzenie liczby całkowitej.
Następnie spróbuj przekonwertować wprowadzoną wartość na typ całkowity przy użyciu funkcji int().
Złap błąd (wyjątek) i wyświetl komunikat informujący użytkownika o tym, że wprowadzona wartość nie jest poprawną liczbą całkowitą.
2. Dzielenie przez zero:

Poproś użytkownika o wprowadzenie dwóch liczb zmiennoprzecinkowych.
Następnie spróbuj podzielić pierwszą liczbę przez drugą.
Złap błąd (wyjątek) związany z dzieleniem przez zero i obsłuż go, wyświetlając odpowiedni komunikat.
3.Tworzenie własnego wyjątku:

Stwórz własny wyjątek nazwany ValueTooSmallError, który będzie podnoszony, gdy przekazana wartość będzie zbyt mała.
Napisz funkcję, która przyjmuje liczbę jako argument.
Jeśli ta liczba jest mniejsza niż 5, podnieś wyjątek ValueTooSmallError.
W przeciwnym razie wydrukuj komunikat o tym, że liczba jest wystarczająco duża.
4.Praktyczne zastosowanie obsługi wyjątków:

Stwórz prosty program, który będzie wczytywał dane z pliku tekstowego.
Obsłuż ewentualne błędy, takie jak brak pliku, problem z odczytem pliku itp.
Jeśli plik istnieje, wydrukuj jego zawartość.
5.Obsługa wielu rodzajów wyjątków:

Napisz program, który prosi użytkownika o podanie nazwy pliku.
Próbuj otworzyć podany plik do odczytu.
Obsłuż różne rodzaje wyjątków, takie jak FileNotFoundError, PermissionError, itp.
Jeśli plik zostanie otwarty poprawnie, wyświetl jego zawartość.



6.Sprawdzanie poprawności wprowadzonych danych:

Poproś użytkownika o wprowadzenie wieku.
Obsłuż przypadki, gdy użytkownik poda coś innego niż liczba całkowita, oraz gdy wiek będzie ujemny.
Wydrukuj odpowiedni komunikat informacyjny w każdym z tych przypadków.
7.Sprawdzanie poprawności danych w liście:

Stwórz listę zawierającą kilka elementów, w tym zarówno liczby, jak i ciągi znaków.
Napisz pętlę, która spróbuje przekonwertować każdy element listy na liczbę całkowitą.
Złap wyjątek, który może wystąpić podczas konwersji, i wydrukuj informację o błędzie oraz element, który spowodował błąd.
8.Tworzenie wyjątków z argumentami:

Stwórz klasę wyjątku nazwaną InvalidEmailError, która będzie podnosić wyjątek, gdy przekazany adres e-mail nie będzie poprawny.
Napisz funkcję, która będzie sprawdzała, czy podany ciąg znaków jest poprawnym adresem e-mail.
Jeśli adres e-mail jest niepoprawny, podnieś wyjątek InvalidEmailError z odpowiednim komunikatem.
9.Obsługa wyjątków w pętli:

Stwórz pętlę, która będzie pytać użytkownika o wprowadzenie liczby całkowitej.
Obsłuż błąd, gdy użytkownik wprowadzi coś innego niż liczba całkowita.
Kontynuuj pętlę, dopóki użytkownik nie wprowadzi poprawnej liczby.
10.Obsługa wyjątków w funkcji zewnętrznej:

Napisz funkcję divide(a, b), która będzie dzieliła dwie liczby.
Wewnątrz funkcji obsłuż wyjątek związany z dzieleniem przez zero.
Wywołaj tę funkcję z użytkownika wprowadzanymi wartościami i wydrukuj wynik lub odpowiedni komunikat błędu.