import multiprocessing

def worker(num):
    """Funkcja wykonywana w każdym procesie"""
    result = num * num
    return result

if __name__ == "__main__":
    # Tworzymy pulę procesów
    pool = multiprocessing.Pool(processes=2)

    # Uruchamiamy zadania w puli procesów
    results = pool.map(worker, [5, 10])

    # Zamykamy pulę procesów
    pool.close()
    pool.join()

    print("Wyniki:", results)
