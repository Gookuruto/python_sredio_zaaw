## Obsługa błędów przy konwersji typów:

1. Poproś użytkownika o wprowadzenie liczby całkowitej.
2. Następnie spróbuj przekonwertować wprowadzoną wartość na typ całkowity przy użyciu funkcji int().
3. Złap błąd (wyjątek) i wyświetl komunikat informujący użytkownika o tym, że wprowadzona wartość nie jest poprawną liczbą całkowitą.

## Dzielenie przez zero:

1. Poproś użytkownika o wprowadzenie dwóch liczb zmiennoprzecinkowych.
2. Następnie spróbuj podzielić pierwszą liczbę przez drugą.
3. Złap błąd (wyjątek) związany z dzieleniem przez zero i obsłuż go, wyświetlając odpowiedni komunikat.

## Tworzenie własnego wyjątku:

1. Stwórz własny wyjątek nazwany ValueTooSmallError, który będzie podnoszony, gdy przekazana wartość będzie zbyt mała.
2. Napisz funkcję, która przyjmuje liczbę jako argument.
3. Jeśli ta liczba jest mniejsza niż 5, podnieś wyjątek ValueTooSmallError.
4. W przeciwnym razie wydrukuj komunikat o tym, że liczba jest wystarczająco duża.

## Praktyczne zastosowanie obsługi wyjątków:

1. Stwórz prosty program, który będzie wczytywał dane z pliku tekstowego.
2. Obsłuż ewentualne błędy, takie jak brak pliku, problem z odczytem pliku itp.
3. Jeśli plik istnieje, wydrukuj jego zawartość.

## Obsługa wielu rodzajów wyjątków:

1. Napisz program, który prosi użytkownika o podanie nazwy pliku.
2. Próbuj otworzyć podany plik do odczytu.
3. Obsłuż różne rodzaje wyjątków, takie jak FileNotFoundError, PermissionError, itp.
4. Jeśli plik zostanie otwarty poprawnie, wyświetl jego zawartość.

## Sprawdzanie poprawności wprowadzonych danych:

1. Poproś użytkownika o wprowadzenie wieku.
2. Obsłuż przypadki, gdy użytkownik poda coś innego niż liczba całkowita, oraz gdy wiek będzie ujemny.
3. Wydrukuj odpowiedni komunikat informacyjny w każdym z tych przypadków.

## Sprawdzanie poprawności danych w liście:

1. Stwórz listę zawierającą kilka elementów, w tym zarówno liczby, jak i ciągi znaków.
2. Napisz pętlę, która spróbuje przekonwertować każdy element listy na liczbę całkowitą.
3. Złap wyjątek, który może wystąpić podczas konwersji, i wydrukuj informację o błędzie oraz element, który spowodował błąd.

## Tworzenie wyjątków z argumentami:

1. Stwórz klasę wyjątku nazwaną InvalidEmailError, która będzie podnosić wyjątek, gdy przekazany adres e-mail nie będzie poprawny.
2. Napisz funkcję, która będzie sprawdzała, czy podany ciąg znaków jest poprawnym adresem e-mail.
3. Jeśli adres e-mail jest niepoprawny, podnieś wyjątek InvalidEmailError z odpowiednim komunikatem.

## Obsługa wyjątków w pętli:

1. Stwórz pętlę, która będzie pytać użytkownika o wprowadzenie liczby całkowitej.
2. Obsłuż błąd, gdy użytkownik wprowadzi coś innego niż liczba całkowita.
3. Kontynuuj pętlę, dopóki użytkownik nie wprowadzi poprawnej liczby.

## Obsługa wyjątków w funkcji zewnętrznej:

1. Napisz funkcję divide(a, b), która będzie dzieliła dwie liczby.
2. Wewnątrz funkcji obsłuż wyjątek związany z dzieleniem przez zero.
3. Wywołaj tę funkcję z użytkownika wprowadzanymi wartościami i wydrukuj wynik lub odpowiedni komunikat błędu.