import sys
import time
import psutil
import os
sys.set_int_max_str_digits(1000000)  # set max int size

class Fibonacci:
    # Dynamic programming solution
    def __init__(self, n):
        self.n = n
        self.fib = [0] * (n + 1)
        self.fib[1] = 1
        self.fib[2] = 1

    def calculate(self):
        for i in range(3, self.n + 1):
            self.fib[i] = self.fib[i - 1] + self.fib[i - 2]

        return self.fib[self.n]

# Recursive solution
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)

def dpTwo(n):
    one = 1
    two = 1

    for _ in range(n - 2):
        temp = one
        one = one + two
        two = temp

    return one

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    method = sys.argv[2] if len(sys.argv) > 2 else "dp"
    ans = None

    # Get the memory usage before the calculation
    process = psutil.Process(os.getpid())
    mem_info_before = process.memory_info()
    before_rss = mem_info_before.rss

    
    start_time = time.time()  # start time
    if method == "recursive":
        ans = str(fib(n))
    elif method == "dp":
        fib = Fibonacci(n)
        ans = str(fib.calculate())
    elif method == "dp2":
        ans = str(dpTwo(n))
    print(ans)
    print(f"n: {n}, method: {method}, number of digits: {len(ans)}")
    end_time = time.time()  # end time

    # Get the memory usage after the calculation
    mem_info_after = process.memory_info()
    after_rss = mem_info_after.rss

    mem_diff = after_rss - before_rss
    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Megabytes used: {mem_diff / 1024 / 1024}")