import asyncio

async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)  # Symulacja operacji zajmującej czas

async def print_letters():
    for letter in 'ABCDE':
        print(letter)
        await asyncio.sleep(1)  # Symulacja operacji zajmującej czas

async def main():
    # Uruchamiamy zadania asynchronicznie
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())

    # Oczekujemy na zakończenie zadań
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
    print("Wszystkie zadania zakończone")
