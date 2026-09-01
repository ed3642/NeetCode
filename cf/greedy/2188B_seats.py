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

def solve(bits, n):

    c = sum(1 if bits[i] == '1' else 0 for i in range(n))
    i = 0
    while i < n:
        if bits[i] == '1':
            i += 2
        else:
            if i+1 < n:
                if bits[i+1] == '0':
                    # put 1 on 0 at i+1
                    c += 1
                    i += 3
                else:
                    i += 3
                    # if i+1 is a 1 i is already covered
            else:
                c += 1 # put a 1 on the last uncovered 0
                i += 1

            while i < n and bits[i-1] == '1':
                i += 1

    return c

def main():
    t = read_int()

    for _ in range(t):
        n = read_int()
        bits = read_string()
        print(solve(bits, n))

if __name__ == "__main__":
    main()
