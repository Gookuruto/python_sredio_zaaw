import time

def slow_function():
    time.sleep(2)

def fast_function():
    time.sleep(0.5)

def main():
    slow_function()
    fast_function()


from pyinstrument import Profiler

# Tworzenie profiler'a
profiler = Profiler()

# Rozpoczęcie profilowania
profiler.start()

# Kod do profilowania
main()

# Zakończenie profilowania
profiler.stop()

# Wyświetlenie wyników profilowania
print(profiler.output_text(unicode=True, color=True))
