import multiprocessing
import time


def parallel(func):
    def wrapper(*args, **kwargs):
        multiprocessing.Process(
            target=func,
            args=args,
            kwargs=kwargs
        ).start()
    return wrapper


def chrono(nbr=1000):
    def deco(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(nbr):
                func(*args, **kwargs)
            print('-' * 40)
            print(func.__name__, args, kwargs)
            print(round(((time.time() - start) / nbr) * 1000, 6), "millisecondes par tours")
        return wrapper
    return deco


if __name__ == '__main__':
    from time import sleep

    @parallel
    def print_p(l):
        for i in range(3):
            print(l)
            sleep(0.05)


    print_p("a")
    print_p("b")
