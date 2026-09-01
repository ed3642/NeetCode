#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr):
    # 1 2 3
    # 1 1 1

    # cut off at index 1
    op1 = arr[0]+arr[1]
    # cut off at index 2
    op2 = 2*arr[0]

    # this is never smaller than op1
    # if n > 2:
    #     op3 = arr[0]+arr[1]+arr[2]
    # else:
    #     op3 = float('inf')

    return min(op1, op2)

def main():
    t = read_int()

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr))

if __name__ == "__main__":
    main()
