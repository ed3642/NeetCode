#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(dorms, letters, m):
    res = [0] * m
    dorm_i = 0
    dorm_start_pos = 0
    dorm_end_pos = dorms[0]

    for i in range(m):
        while letters[i] > dorm_end_pos:
            dorm_start_pos = dorm_end_pos
            dorm_i += 1
            dorm_end_pos += dorms[dorm_i]
        res[i] = [dorm_i+1, letters[i]-dorm_start_pos]

    return res

def main():
    n, m = read_ints()
    dorms = read_ints()
    letters = read_ints()

    res = solve(dorms, letters, m)

    for r in res:
        print(*r)

if __name__ == "__main__":
    main()
