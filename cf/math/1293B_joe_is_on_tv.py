#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(n):

    _sum = 0
    for x in range(1, n+1):
        _sum += 1/x
    return _sum

def main():
    print(solve(read_int()))

if __name__ == "__main__":
    main()
