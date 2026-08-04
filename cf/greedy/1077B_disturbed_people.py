#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr, n):
    c = 0
    for i in range(1, n-1):
        if arr[i] == 0 and arr[i-1] == 1 and arr[i+1] == 1:
            arr[i+1] = 0 # turn off these lights, i-1 doesnt matter anymore
            c += 1
    return c

def main():
    n = read_int()
    arr = read_ints()

    print(solve(arr, n))

if __name__ == "__main__":
    main()
