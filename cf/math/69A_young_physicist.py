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
    x_sum = 0
    y_sum = 0
    z_sum = 0

    for x, y, z in data:
        x_sum += x
        y_sum += y
        z_sum += z
    
    return 'YES' if x_sum == y_sum == z_sum == 0 else 'NO'

def main():
    num_vec = read_int()
    data = []

    for _ in range(num_vec):
        data.append(read_ints())
    print(solve(data))

if __name__ == "__main__":
    main()
