#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr: list[int]):
    INF = float('inf')
    arr.append(INF) # stopper
    arrays = 0

    cons = 1
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            i += 1
            continue
        elif arr[i] == arr[i+1]-1:
            cons += 1
        else:
            arrays += (cons+1)//2
            cons = 1
        i += 1

    return arrays

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr))

if __name__ == "__main__":
    main()
