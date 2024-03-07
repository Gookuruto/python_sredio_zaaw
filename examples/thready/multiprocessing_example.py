import multiprocessing
import os

def worker():
    """Funkcja wykonywana w każdym procesie"""
    print(f"ID procesu potomnego: {os.getpid()}")

if __name__ == "__main__":
    # Tworzymy procesy potomne
    process1 = multiprocessing.Process(target=worker)
    process2 = multiprocessing.Process(target=worker)

    # Uruchamiamy procesy potomne
    process1.start()
    process2.start()

    # Czekamy na zakończenie procesów potomnych
    process1.join()
    process2.join()

    print("Proces główny zakończony")
