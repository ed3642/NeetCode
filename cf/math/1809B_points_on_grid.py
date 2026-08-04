#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import math
import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# O(1)
def solve(n):
    x = math.floor(math.sqrt(n))
    # sqrt will lose accuracy in large nums
    # fix overshot
    while x*x > n:
        x -= 1
    # fix undershot, will overshoot by 1 on purpose
    while x*x < n:
        x += 1
    # -1 from the undershot adjustment
    return x-1

# O(log 10^9+1)
def solve(n):
    # y=(x+1)^2 binary search x
    l = 0
    r = 10**9+1 # from test limitations

    # minimize bs pattern
    while l <= r:
        m = (l+r)//2
        if m*m >= n:
            r = m-1
        else:
            l = m+1

    return r

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        print(solve(read_int()))

if __name__ == "__main__":
    main()
