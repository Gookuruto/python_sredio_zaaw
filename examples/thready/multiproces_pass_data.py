import multiprocessing

def worker(num):
    """Funkcja wykonywana w każdym procesie"""
    result = num * num
    print(f"Wynik dla {num}: {result}")

if __name__ == "__main__":
    # Tworzymy procesy potomne
    process1 = multiprocessing.Process(target=worker, args=(5,))
    process2 = multiprocessing.Process(target=worker, args=(10,))

    # Uruchamiamy procesy potomne
    process1.start()
    process2.start()

    # Czekamy na zakończenie procesów potomnych
    process1.join()
    process2.join()

    print("Proces główny zakończony")
