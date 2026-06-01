#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(data):
    ...

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        data = read_all()
        ans = solve(data)
        if ans is not None:
            print(ans)

if __name__ == "__main__":
    main()
