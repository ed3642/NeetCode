import time

def time_functions(func1, func2, *args, **kwargs):
    start_time = time.time()
    func1(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time of {func1.__name__}: {end_time - start_time} seconds")

    start_time = time.time()
    func2(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time of {func2.__name__}: {end_time - start_time} seconds")