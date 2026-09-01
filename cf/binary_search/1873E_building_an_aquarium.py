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

def solve(arr, wlim):

    def works(h):
        water = 0
        for i in range(N):
            water += h-arr[i] if arr[i] < h else 0
            if water > wlim:
                return False
        return True

    N = len(arr)
    l = 0
    r = (wlim+N-1+sum(arr))//N
    
    while l <= r:
        m = (l+r)//2
        if works(m):
            l = m+1
        else:
            r = m-1

    return r

def main():
    res = []

    t = rint()
    for _ in range(t):
        n, w = rints()
        arr = rints()
        res.append(solve(arr, w))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
