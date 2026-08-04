#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr, k):
    if k == 0:
        return 0
    sorted_months = sorted(arr, reverse=True)
    _sum = 0
    for i in range(len(arr)):
        _sum += sorted_months[i]
        if _sum >= k:
            return i+1
    return -1

def main():
    k = read_int()
    arr = read_ints()
    print(solve(arr, k))

if __name__ == "__main__":
    main()
