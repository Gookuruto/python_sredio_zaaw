import threading
import time

def sleep_hour():
    print("im going to sleep")
    time.sleep(3600)
    print("i wake up")
    

t = threading.Thread(target=sleep_hour)
t.start()

t.join()