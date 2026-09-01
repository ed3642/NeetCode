#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import math
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

def solve(n, k):
    # [0, 2**k-1] numbers up to k binary size
    # n bitstrings of size k
    # each bit position can be chosen n different ways: (n-1) 1s and 1 0s = n ways total

    return ((n)**k) % MOD

def main():
    res = []

    t = rint()
    for _ in range(t):
        n, k = rints()
        res.append(solve(n, k))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
