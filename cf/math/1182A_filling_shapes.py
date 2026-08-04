#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# [1,1,3,5]
# [-1,0,-1,-2]
# [5,3,1,1]
# [-5,-2,1,2]

def solve(n):
    if n % 2 != 0:
        return 0

    return 2**(n//2)

def main():
    n = read_int()

    print(solve(n))

if __name__ == "__main__":
    main()
