#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())

def read_input():
    return read_chars()

def solve(data):
    return 1 if '+' in data else -1

def main():
    line = input().strip()
    t = int(line) if line else 1

    x = 0
    for _ in range(t):
        data = read_input()
        x += solve(data)
    print(x)

if __name__ == "__main__":
    main()
