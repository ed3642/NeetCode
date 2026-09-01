#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

MOD = 10**9+7
INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr, n):
    l = 0
    r = n-1
    _min = 1
    _max = n

    while l < r:
        if arr[l] == _min:
            _min += 1
            l += 1
        elif arr[l] == _max:
            _max -= 1
            l += 1
        elif arr[r] == _min:
            _min += 1
            r -= 1
        elif arr[r] == _max:
            _max -= 1
            r -= 1
        else:
            return [l+1, r+1] # want 1-indexed

    return [-1]

def main():
    res = []

    t = rint()
    for _ in range(t):
        n = rint()
        arr = rints()
        res.append(solve(arr, n))
            
    for r in res:
        print(*r)

if __name__ == "__main__":
    main()
