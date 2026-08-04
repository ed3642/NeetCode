#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(data, x, y):

    bot = data[0]
    top = data[1]
    left = data[2]
    right = data[3]
    res = 0

    # check bot base and top point
    max_base = bot[bot[0]]-bot[1]
    res = max_base*y
    # top base and bot point
    max_base = top[top[0]]-top[1]
    res = max(max_base*y, res)
    # left base and right point
    max_base = left[left[0]]-left[1]
    res = max(max_base*x, res)
    # right base and left point
    max_base = right[right[0]]-right[1]
    res = max(max_base*x, res)

    return res

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        x, y = read_ints()
        points = []
        for _ in range(4):
            # points given in order bot top left right 
            points.append(read_ints())
        res = solve(points, x, y)
        if res:
            print(res)

if __name__ == "__main__":
    main()
