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

def solve(balls, s):
    c = 0
    # 1 1 or -1 -1 vectors must lie on a (x,x) coord
    # 1 -1 or -1 1 vectors must lie on a coord that sums to s e.i on top left to bot right diag
    # with these conditions when a ball collides its basically like they swap places and they continue on their path so its like nothing happens if we just care about how many balls make it to a hole.
    # balls not on a diag will just bounce in a tilted square shape
    for dx, dy, x, y in balls:
        if x == y and ((dx, dy) == (1, 1) or (dx, dy) == (-1, -1)):
            c += 1
        elif x+y == s and ((dx, dy) == (1, -1) or (dx, dy) == (-1, 1)):
            c += 1
    return c


def main():
    t = read_int()

    out = []
    for _ in range(t):
        n, s = read_ints()
        balls = []
        for _ in range(n):
            balls.append(read_ints())
        out.append(solve(balls, s))

    print('\n'.join(map(str, out)))

if __name__ == "__main__":
    main()
