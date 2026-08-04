#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(n, r, m, b):
    max_f = 0

    for i in range(1, n):
        r[i] += r[i-1]
    for j in range(1, m):
        b[j] += b[j-1]

    for i in range(n+1):
        for j in range(m+1):
            r_val = r[i-1] if i > 0 else 0
            b_val = b[j-1] if j > 0 else 0
            max_f = max(max_f, r_val+b_val)

    return max_f

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n = read_int()
        r = read_ints()
        m = read_int()
        b = read_ints()
        print(solve(n, r, m, b))

if __name__ == "__main__":
    main()
