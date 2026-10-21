import time
from contextlib import contextmanager


@contextmanager
def timer():
    start=time.perf_counter()

    try:
        yield
    finally:
        end=time.perf_counter()
        print("Время выполнения:",end-start,"секунд")


with timer():
    total=sum(range(10000000))
