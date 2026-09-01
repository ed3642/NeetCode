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

def solve(prices, coins):

    # max valid value binary search pattern
    N = len(prices)
    l = 0
    r = N-1

    while l <= r:
        m = (l+r)//2
        if coins >= prices[m]:
            l = m+1
        else:
            r = m-1

    return r+1 # +1 bc we want the num of elems not the index

def main():
    res = []

    n = rint()
    prices = rints()
    prices.sort()
    d = rint()
    for _ in range(d):
        coins = rint()
        res.append(solve(prices, coins))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
