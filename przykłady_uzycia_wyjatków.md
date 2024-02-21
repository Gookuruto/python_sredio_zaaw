Wyjątki w Pythonie są używane do zarządzania sytuacjami wyjątkowymi i nieoczekiwanymi zdarzeniami w trakcie wykonywania programu. Poniżej znajdziesz kilka praktycznych przykładów wykorzystania wyjątków w Pythonie:

1. **Otwieranie pliku:**
   Podczas próby otwarcia pliku, może wystąpić wiele różnych błędów, na przykład brak pliku, brak uprawnień do odczytu, czy plik został już otwarty przez inny program. W takich przypadkach przydatne jest użycie bloku `try-except` do obsługi wyjątków.

   ```python
   try:
       with open("file.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found")
   except PermissionError:
       print("Permission denied")
   except Exception as e:
       print(f"An error occurred: {e}")
   ```

2. **Operacje na plikach:**
   Podczas operacji na plikach, takich jak odczyt, zapis czy zamknięcie, również może dojść do różnych błędów. Używając bloku `try-except`, można obsłużyć te sytuacje.

   ```python
   try:
       file = open("file.txt", "r")
       content = file.read()
   except IOError:
       print("Error reading file")
   finally:
       file.close()
   ```

3. **Operacje na liście:**
   Podczas operacji na liście, takich jak dostęp do indeksu, dodawanie czy usuwanie elementów, należy pamiętać, że mogą pojawić się błędy, np. próba dostępu do indeksu spoza zakresu.

   ```python
   my_list = [1, 2, 3]
   try:
       print(my_list[4])
   except IndexError:
       print("Index out of range")
   ```

4. **Zapytania do bazy danych:**
   Podczas wykonywania zapytań do bazy danych, mogą wystąpić różne błędy, np. problemy z połączeniem, błędne zapytanie itp. W takich przypadkach przydatne jest użycie bloku `try-except` do obsługi wyjątków.

   ```python
   import sqlite3

   try:
       conn = sqlite3.connect('example.db')
       cursor = conn.cursor()
       cursor.execute("SELECT * FROM table")
   except sqlite3.Error as e:
       print("An error occurred:", e)
   finally:
       conn.close()
   ```

5. **Dzielenie przez zero:**
   Próba dzielenia przez zero spowoduje wygenerowanie wyjątku `ZeroDivisionError`, który można obsłużyć, aby program nie przestał działać.

   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero")
   ```

Obsługa wyjątków pozwala na elastyczne i kontrolowane reagowanie na nieoczekiwane sytuacje w trakcie wykonywania programu, co pomaga w tworzeniu bardziej niezawodnych i bezpiecznych aplikacji.