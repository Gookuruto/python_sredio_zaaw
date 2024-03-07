import timeit
import multiprocessing


def count():
    pass
def spawn_processes():
    processes = []
    count_start = 400000
    for _ in range(2):  # Spawn 1000 processes
        process = multiprocessing.Process(target=count)  # Placeholder function for no computation
        process.start()
        #processes.append(process)
    # for process in processes:
    #     process.join()

if __name__ == "__main__":
    setup = "from __main__ import spawn_processes"
    time_spent = timeit.timeit(stmt="spawn_processes()", setup=setup, number=100)
    print("Time spent spawning processes:", time_spent, "seconds")
