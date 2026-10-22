import time
from functools import wraps
def measure_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.perf_counter()

        try:
            return func(*args,**kwargs)
        finally:
            end=time.perf_counter()
            print("Время выполнения",func.__name__+":",end-start,"секунд")

    return wrapper
@measure_time
def calculate():
    total=0

    for i in range(1000000):
        total+=i

    return total
@measure_time
def multiply(a,b):
    return a*b
@measure_time
def show_message(message,count=1):
    for i in range(count):
        print(message)
calculate()
print(multiply(15,3))
show_message("Привет",2)
