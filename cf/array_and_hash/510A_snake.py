#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(n, m):
    res = ['#' * m]
    state = 0

    for _ in range(2, n, 2):
        if state == 0:
            pattern = '.' * (m-1) + '#'
            res.append(pattern)
        else:
            pattern = '#' + '.' * (m-1)
            res.append(pattern)
        res.append('#' * m)
        state ^= 1
    
    return res

def main():
    n, m = read_ints()

    res = solve(n, m)

    for row in res:
        print(row)

if __name__ == "__main__":
    main()
