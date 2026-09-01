#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# 2 1 3 2 5

def solve(arr):
    arr.sort()
    N = len(arr)

    l = 0 
    r = N-1

    res = [0] * N
    i = 0
    while l <= r:
        if i%2 == 0:
            res[i] = arr[l]
            l += 1
        else:
            res[i] = arr[r]
            r -= 1
        i += 1

    return res

def main():

    n = read_int()
    arr = read_ints()
    print(*solve(arr))

if __name__ == "__main__":
    main()
