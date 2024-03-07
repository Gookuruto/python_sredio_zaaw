import timeit


def count(_from, _to):
    while _from >= _to:
        _from -= 1


def wo_threading_func():
    count(400000, 0)


def with_threading_func():
    import multiprocessing

    t1 = multiprocessing.Process(target=count, args=(400000, 200000))
    t2 = multiprocessing.Process(target=count, args=(200000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    wo_threading = "wo_threading_func()"
    with_threading ="with_threading_func()"

    setup = "from __main__ import wo_threading_func,with_threading_func"

    print("Bez watkow:", timeit.timeit(stmt=wo_threading,
                                       setup=setup,
                                       number=1))
    print("Z watkami:", timeit.timeit(stmt=with_threading,
                                      setup=setup,
                                      number=1))