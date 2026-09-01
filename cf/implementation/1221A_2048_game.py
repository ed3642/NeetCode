#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
from typing import Counter
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr):
    # 2^11 = 2048 need 2^0
    # 2^10 = 1024 need 2^1
    # 2^9  = 512  need 2^2
    # ...
    # 2^1  = 2    need 2^(11-1)
    # 2^0  = 1    need 2^11

    hz = Counter(arr)
    
    # promote nums as much as possible
    for p in range(11):
        c = hz[2**p]
        hz[2**(p+1)] += c>>1

    return 'YES' if hz[2<<10] >= 1 else 'NO'

def main():
    t = read_int()

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr))

if __name__ == "__main__":
    main()
