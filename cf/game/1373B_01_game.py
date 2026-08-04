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
    ones = 0
    zeros = 0
    for c in data:
        if c == '0':
            zeros += 1
        else:
            ones += 1
    possible_moves = min(zeros, ones)
    return 'DA' if possible_moves % 2 != 0 else 'NET'

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        data = read_chars()
        print(solve(data))

if __name__ == "__main__":
    main()
