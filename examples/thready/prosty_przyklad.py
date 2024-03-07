import threading
import time
super_wartosc = []
def print_numbers():
    global super_wartosc

    for i in range(5):
        print(i)
        super_wartosc.append("cos")

def print_letters():
    global super_wartosc
    for letter in 'ABCDEf':
        print(letter)
        super_wartosc.pop()

# Tworzymy wątki
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

print(super_wartosc)
# Uruchamiamy wątki
thread1.start()
thread2.start()

# Czekamy na zakończenie wątków
thread1.join()
thread2.join()
print(super_wartosc)

print("Wszystkie wątki zakończone")
