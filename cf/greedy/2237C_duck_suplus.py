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

def solve(arr):
    N = len(arr)

    for i in range(1, N):
        if arr[i-1] > arr[i]:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] += temp

    return arr[N-1]

def main():
    t = read_int()

    res = []
    for _ in range(t):
        n = read_int()
        arr = read_ints()
        res.append(solve(arr))

    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
