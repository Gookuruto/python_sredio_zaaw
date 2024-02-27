import time

class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f"Time taken: {end_time - self.start_time} seconds")

# Przykład użycia:
with TimerContextManager():
    time.sleep(1)
    x = [i for i in range(int(10e10))]
