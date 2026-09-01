#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from bisect import bisect_left
from functools import reduce
import math
import operator
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

def solve(arr, n: int):
    # 2^n | p
    # 1 2^1 3 2^2 5 2*3 7 2^3 9 2*5 ... 
    # 1-indexed
    # q := the number of 2s that cant be divided out by the initial product
    # mutiply the biggest powers of 2 indexes first to minimize ops
    # then see how many even indexes left and check those
    # reframe problem to num of 2s in numerator have to be eq or gt 2s in denominator
    # good problem

    twos = n
    mulsof2 = [0] * n # multiples of 2 in indexes

    for i, num in enumerate(arr):
        while num%2 == 0:
            twos -= 1
            if twos == 0:
                return 0
            num = num >> 1

    # need operations to cancel out remaining twos from 2^n

    for i in range(1, n+1):
        j = i
        while i%2 == 0:
            mulsof2[j-1] += 1
            i = i >> 1

    mulsof2.sort(reverse=True)
    for i in range(1, n):
        mulsof2[i] += mulsof2[i-1]

    pos = bisect_left(mulsof2, twos)+1 # num of indexes needed to use
    return pos if pos <= n else -1

def main():
    res = []

    t = rint()
    for _ in range(t):
        n = rint()
        arr = rints()
        res.append(solve(arr, n))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
