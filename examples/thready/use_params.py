import threading

def greet(name):
    print(f"Hello, {name}!")

# Tworzymy wątek z argumentem
thread = threading.Thread(target=greet, args=("Alice",))

# Uruchamiamy wątek
thread.start()
