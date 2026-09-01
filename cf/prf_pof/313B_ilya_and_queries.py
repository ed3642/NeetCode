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

def solve(pf, l, r):
    # # . . # # #
    # 0 1 0 1 1 0
    # 0 1 1 2 3 3
    
    # r is exclusive in problem
    return pf[r-1]-pf[l-1]

def main():
    res = []

    string = rstring()
    N = len(string)

    pf = [0] * (N+1)
    for i in range(N-1):
        pfi = i+1 # pf is 1 indexed
        if string[i] == string[i+1]:
            pf[pfi] = pf[pfi-1]+1
        else:
            pf[pfi] = pf[pfi-1]
    pf[N] = pf[N-1]

    n = rint()
    for _ in range(n):
        l, r = rints()
        res.append(solve(pf, l, r))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
