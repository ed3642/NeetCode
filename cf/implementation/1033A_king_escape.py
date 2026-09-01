#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import deque
import sys
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# normal chess board directions
# 4 5 6 7
# 3 4 5 6
# 2 3 4 5
# 1 2 3 4

# transformed chess board
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

def solve(n, q, k, t):
    qx, qy = q
    kx, ky = k
    tx, ty = t

    if qx+qy == tx+ty: # same topleft to botright diag
        return 'NO'
    # transformed y to easily see the botleft to topright diag
    trqy = (n+1)-qy
    trty = (n+1)-ty
    if qx+trqy == tx+trty:
        return 'NO'

    # target not on kings corner
    if (kx < qx and tx >= qx or
        ky < qy and ty >= qy or
        kx > qx and tx <= qx or
        ky > qy and ty <= qy):
        return 'NO'

    return 'YES'

def main():
    n = read_int()

    q = read_ints()
    k = read_ints()
    t = read_ints()

    print(solve(n, q, k, t))

if __name__ == "__main__":
    main()
