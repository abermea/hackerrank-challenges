from time import perf_counter
from functools import wraps

def perf_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper