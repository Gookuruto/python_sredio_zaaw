import threading
import time
import random
import os


# Zadanie 1: Wielowątkowe obliczenia - suma elementów listy
def calculate_sum(numbers):
    return sum(numbers)


def parallel_sum(numbers, num_threads):
    chunk_size = len(numbers) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(numbers)
        thread = threading.Thread(target=lambda n: results.append(calculate_sum(n)), args=(numbers[start:end],))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return sum(results)


# Zadanie 2: Wielowątkowe przetwarzanie plików - ilość słów w plikach
def count_words_in_file(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        return len(text.split())


def process_files(files):
    results = {}
    threads = []

    for file_name in files:
        thread = threading.Thread(target=lambda f: results.update({f: count_words_in_file(f)}), args=(file_name,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results


# Zadanie 3: Synchronizacja wątków - modyfikacja współdzielonej listy
def modify_shared_list(shared_list, num_threads):
    lock = threading.Lock()

    def worker():
        nonlocal shared_list
        for _ in range(10):
            with lock:
                shared_list.append(random.randint(1, 100))

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return shared_list


# Zadanie 4: Wielowątkowa komunikacja między wątkami - kolejka komunikatów
class MessageQueue:
    def __init__(self):
        self.messages = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(lock=self.lock)

    def put(self, message):
        with self.lock:
            self.messages.append(message)
            self.condition.notify()

    def get(self):
        with self.lock:
            while not self.messages:
                self.condition.wait()
            return self.messages.pop(0)


# Zadanie 5: Wielowątkowe pobieranie danych z internetu
def download_file(url, save_path):
    # Symulacja pobierania pliku z internetu
    time.sleep(random.random() * 5)
    # Zapisanie pliku
    with open(save_path, 'w') as file:
        file.write(f"File downloaded from {url}")


def parallel_downloads(urls):
    threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=download_file, args=(url, f"file_{i}.txt"))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


# Zadanie 6: Wielowątkowe przetwarzanie obrazów - zmiana rozmiaru
def resize_image(image_path, new_width, new_height):
    # Symulacja przetwarzania obrazu
    time.sleep(random.random())
    print(f"Resized image {image_path} to {new_width}x{new_height}")


def parallel_image_processing(image_paths, new_width, new_height):
    threads = []
    for image_path in image_paths:
        thread = threading.Thread(target=resize_image, args=(image_path, new_width, new_height))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


# Zadanie 7: Wielowątkowe sortowanie
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def parallel_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    left_thread = threading.Thread(target=parallel_quick_sort, args=(left,))
    right_thread = threading.Thread(target=parallel_quick_sort, args=(right,))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return left + middle + right


# Zadanie 8: Wielowątkowa obsługa baz danych - zapis danych do bazy danych
class Database:
    def __init__(self):
        self.data = []
        self.lock = threading.Lock()

    def insert_data(self, data):
        with self.lock:
            self.data.extend(data)


# Zadanie 9: Wielowątkowe przetwarzanie danych strumieniowych
def process_stream(stream):
    while True:
        data = stream.read(1024)
        if not data:
            break
        # Symulacja przetwarzania danych
        time.sleep(random.random())
        print("Processed data:", data)


# Zadanie 10: Wielowątkowe obliczenia numeryczne - obliczanie sumy liczb
def calculate_total_sum(numbers):
    return sum(numbers)


def parallel_calculate_total_sum(numbers, num_threads):
    chunk_size = len(numbers) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(numbers)
        thread = threading.Thread(target=lambda n: results.append(calculate_total_sum(n)), args=(numbers[start:end],))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return sum(results)


# Przykładowe użycie funkcji
if __name__ == "__main__":
    # Zadanie 1: Wielowątkowe obliczenia
    numbers = [random.randint(1, 100) for _ in range(1000)]
    num_threads = 4
    print("Parallel sum:", parallel_sum(numbers, num_threads))

    # Zadanie 2: Wielowątkowe przetwarzanie plików
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    print("Words count in files:", process_files(files))

    # Zadanie 3: Synchronizacja wątków
    shared_list = []
    num_threads = 3
    print("Shared list after modification:", modify_shared_list(shared_list, num_threads))

    # Zadanie 4: Wielowątkowa komunikacja między wątkami
    message_queue = MessageQueue()


    def producer():
        for i in range(5):
            message_queue.put(f"Message {i}")


    def consumer():
        for _ in range(5):
            message = message_queue.get()
            print("Received:", message)


    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    # Zadanie 5: Wielowątkowe pobieranie danych z internetu
    urls = ['http://example.com/file1.txt', 'http://example.com/file2.txt', 'http://example.com/file3.txt']
    parallel_downloads(urls)

    # Zadanie 6: Wielowątkowe przetwarzanie obrazów
    image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    parallel_image_processing(image_paths, 800, 600)

    # Zadanie 7: Wielowątkowe sortowanie
    arr = [random.randint(1, 100) for _ in range(100)]
    print("Sorted array:", parallel_quick_sort(arr))

    # Zadanie 8: Wielowątkowa obsługa baz danych
    db = Database()
    data = [random.randint(1, 100) for _ in range(100)]
    db.insert_data(data)
    print("Database data:", db.data)

    # Zadanie 9: Wielowątkowe przetwarzanie danych strumieniowych
    stream = open("stream.txt", "rb")
    process_stream(stream)
    stream.close()

    # Zadanie 10: Wielowątkowe obliczenia numeryczne
    numbers = [random.randint(1, 100) for _ in range(1000)]
    num_threads = 4
    print("Parallel total sum:", parallel_calculate_total_sum(numbers, num_threads))
