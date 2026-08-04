#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(times, n):

    prev_h, prev_m = times[0]
    cons = 1 # consecutives
    max_cons = 1

    for i in range(1, n):
        curr_h, curr_m = times[i]
        if curr_h == prev_h and curr_m == prev_m:
            cons += 1
            max_cons = max(max_cons, cons)
        else:
            cons = 1
        prev_h, prev_m = curr_h, curr_m

    return max_cons

def main():
    n = read_int()
    times = []
    for _ in range(n):
        times.append(read_ints())

    print(solve(times, n))

if __name__ == "__main__":
    main()
