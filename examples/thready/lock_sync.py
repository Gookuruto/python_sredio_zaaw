import threading

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    lock.acquire()  # Blokowanie dostępu do sekcji krytycznej
    counter += 1
    lock.release()  # Odblokowanie dostępu do sekcji krytycznej


def main():
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=increment_counter)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Wartość licznika:", counter)


if __name__ == "__main__":
    main()
