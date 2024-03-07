'''
import threading
import time

def task(name):
    print(f"Rozpoczynam zadanie: {name}")
    time.sleep(2)  # Symulacja długotrwałej operacji
    print(f"Zakończono zadanie: {name}")

def main():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=task, args=(f"Zadanie {i+1}",))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

'''
import asyncio


async def task(name):
    print(f"Rozpoczynam zadanie: {name}")
    await asyncio.sleep(2)  # Symulacja długotrwałej operacji
    print(f"Zakończono zadanie: {name}")


async def main():
    tasks = []
    for i in range(5):
        tasks.append(task(f"Zadanie {i + 1}"))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
