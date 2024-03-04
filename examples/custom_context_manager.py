import contextlib
import time


class CustomContextManager:
    def __init__(self):
        self._is_connected = False

    def __enter__(self):
        self._is_connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._is_connected =False


class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


@contextlib.contextmanager
def timer_cont():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")


# Użycie naszego customowego menedżera kontekstu:
with CustomContextManager() as c:
    # Tutaj możemy umieścić kod, którego czas wykonania chcemy zmierzyć
    # time.sleep(2)  # Symulacja operacji, która zajmuje trochę czasu
    print(c._is_connected)

print(c._is_connected)

