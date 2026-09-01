#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr, k):
    N = len(arr)

    _sum = sum(arr[:k])
    min_sum = _sum
    j = 0

    for i in range(k, N):
        _sum += arr[i]-arr[i-k]
        if _sum < min_sum:
            min_sum = _sum
            j = i-k+1

    return j+1 # +1 cause they want 1-indexed

def main():
    res = []

    n, k = rints()
    arr = rints()
    res.append(solve(arr, k))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
