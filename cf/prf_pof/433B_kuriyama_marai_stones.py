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

def solve(stones, queries, n, m):

    pf = [0] + stones
    spf = sorted(pf)
    res = [0] * m

    for i in range(1, n+1):
        pf[i] += pf[i-1]
        spf[i] += spf[i-1]

    for i in range(m):
        type, l, r = queries[i]
        if type == 1:
            res[i] = pf[r]-pf[l-1]
        else:
            res[i] = spf[r]-spf[l-1]

    return res

def main():

    n = rint()
    stones = rints()
    m = rint()
    q = [0] * m
    for i in range(m):
        q[i] = rints()
            
    print('\n'.join(map(str, solve(stones, q, n, m))))

if __name__ == "__main__":
    main()
