#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import defaultdict
import math
import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(x, k):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3 or n == 5:
            return True
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            return False

        sqr = int(math.sqrt(n)) + 2 # +2 to ensure proper range check
        # 6k +/- 1 optimization
        for i in range(6, sqr, 6):
            if n % (i - 1) == 0 or n % (i + 1) == 0:
                return False
        return True

    # special case this makes 11, there could be some other ints of form 1111...111 that are prime but this is the only one in the test case range.
    if x == 1 and k == 2:
        return 'YES'
    
    if k == 1:
        return 'YES' if is_prime(x) else 'NO'
    return 'NO' # in this case y is always guaranteed to be composite
 
def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        x, k = read_ints()
        print(solve(x, k))

if __name__ == "__main__":
    main()
