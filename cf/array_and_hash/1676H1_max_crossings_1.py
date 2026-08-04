#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# 1 4 4 5 6 6 7

# O(n^2)
def solve(arr, n):
    # for ith wire: num wires that start after it and land before or eq to it

    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] <= arr[i]:
                c += 1

    return c

def main():
    t = read_int()

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr, n))

if __name__ == "__main__":
    main()
