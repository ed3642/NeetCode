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

def solve(n, k):

    l = 0
    r = n*k

    while l < r:
        m = (l+r)//2
        ndbn = m-(m//n)
        if ndbn < k:
            l = m+1
        else:
            r = m

    return l

def main():
    res = []

    t = rint()
    for _ in range(t):
        res.append(solve(*rints()))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
