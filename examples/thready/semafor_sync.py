import threading
import time

semaphore = threading.Semaphore(
    2)  # Ustawienie semafora na 2, co pozwoli na dostęp do zasobów dla dwóch wątków jednocześnie


def access_resource():
    semaphore.acquire()  # Blokowanie dostępu do zasobów
    print("Zasób jest dostępny")
    time.sleep(2)
    semaphore.release()  # Odblokowanie dostępu do zasobów


def main():
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=access_resource)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
