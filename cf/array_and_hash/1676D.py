#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(grid, n, m):
    diag1 = [[0 for _ in range(m)] for _ in range(n)] # botleft to topright
    diag2 = [[0 for _ in range(m)] for _ in range(n)] # topleft to botright

    # first half of diag1
    for i_start in range(n):
        # get the sum of this diag
        _sum = 0
        i = i_start
        j = 0
        while i >= 0 and j < m:
            _sum += grid[i][j]
            i -= 1
            j += 1
        # write the sum on this diag
        i = i_start
        j = 0
        while i >= 0 and j < m:
            diag1[i][j] = _sum
            i -= 1
            j += 1
    # second half of diag1
    for j_start in range(1, m):
        _sum = 0
        i = n-1
        j = j_start
        while i >= 0 and j < m:
            _sum += grid[i][j]
            i -= 1
            j += 1
        i = n-1
        j = j_start
        while i >= 0 and j < m:
            diag1[i][j] = _sum
            i -= 1
            j += 1

    # first half of diag2
    for i_start in range(n):
        _sum = 0
        i = i_start
        j = 0
        while i < n and j < m:
            _sum += grid[i][j]
            i += 1
            j += 1
        i = i_start
        j = 0
        while i < n and j < m:
            diag2[i][j] = _sum
            i += 1
            j += 1
    # second half of diag2
    for j_start in range(1, m):
        _sum = 0
        i = 0
        j = j_start
        while i < n and j < m:
            _sum += grid[i][j]
            i += 1
            j += 1
        i = 0
        j = j_start
        while i < n and j < m:
            diag2[i][j] = _sum
            i += 1
            j += 1

    max_val = 0
    for i in range(n):
        for j in range(m):
            max_val = max(max_val, diag1[i][j]+diag2[i][j]-grid[i][j])

    return max_val

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n, m = read_ints()
        grid = []
        for _ in range(n):
            grid.append(read_ints())
        print(solve(grid, n, m))

if __name__ == "__main__":
    main()
