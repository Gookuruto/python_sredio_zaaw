import threading
import time
from typing import Optional


class ThreadWithReturn(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self) -> None:
        self.result = self.target(*self.args,**self.kwargs)

    def join(self, timeout: Optional[float] = None) -> None:
        super().join(timeout)
        return self.result


def calculate_cube(n):
    time.sleep(2)
    print("Watek cube sie skonzcyl")
    return n*n*n

def calculate_square(n):
    time.sleep(1)
    print("Watek square sie skonzcyl")
    return n*n

t1 = ThreadWithReturn(target=calculate_cube,args=(5,))
t2 = ThreadWithReturn(target=calculate_square, args=(10,))


t1.start()
t2.start()

time.sleep(10)
print(t1.join())
print(t2.join())

print("Done")