import time


class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


# Użycie naszego customowego menedżera kontekstu:
with TimerContextManager():
    # Tutaj możemy umieścić kod, którego czas wykonania chcemy zmierzyć
    time.sleep(2)  # Symulacja operacji, która zajmuje trochę czasu
