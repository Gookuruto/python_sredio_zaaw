import threading

class ThreadManager:
    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.thread = threading.Thread(target=self.target)
        self.thread.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.thread.join()

# Przykład użycia:
def example_thread():
    for i in range(3):
        print(f"Thread: {i}")

with ThreadManager(example_thread):
    print("Inside context manager")
