import threading
import queue

data_queue = queue.Queue()


def producer():
    for i in range(5):
        data_queue.put(i)


def consumer():
    while not data_queue.empty():
        item = data_queue.get()
        print("Pobrano:", item)


def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    main()
