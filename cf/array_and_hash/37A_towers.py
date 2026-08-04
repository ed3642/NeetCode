#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import Counter
import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(towers):

    f = Counter(towers)
    return (max(f.values()), len(f))

def main():
    n = read_int()

    towers = read_ints()

    print(*solve(towers))

if __name__ == "__main__":
    main()
