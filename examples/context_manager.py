# Przy użyciu menedżera kontekstu nie musimy ręcznie zamykać pliku,
# ponieważ zostanie on zamknięty automatycznie po wyjściu z bloku with.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

file.read()


# import os
#
# # Tutaj menedżer kontekstu automatycznie zmieni katalog na "test",
# # a po wyjściu z bloku with wróci do poprzedniego katalogu.
#
# with os.chdir("test"):
#     print("Current directory:", os.getcwd())
#
# # Po wyjściu z bloku with katalog wróci do poprzedniego.
#
# print("Back to original directory:", os.getcwd())


# import sqlite3
#
# # Przy użyciu menedżera kontekstu nie musimy ręcznie zamykać połączenia z bazą danych.
#
# with sqlite3.connect("example.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Po wyjściu z bloku with połączenie z bazą danych zostanie automatycznie zamknięte.
