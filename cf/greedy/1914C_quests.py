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

def solve(exp, expb, k):

    N = len(exp)
    max_points = 0
    points = 0
    max_b_seen = 0

    for i in range(min(N, k)):
        max_b_seen = max(max_b_seen, expb[i])
        points += exp[i]
        max_points = max(max_points, points+(k-(i+1))*max_b_seen)

    return max_points

def main():
    res = []

    t = rint()
    for _ in range(t):
        n, k = rints()
        exp = rints()
        expb = rints()
        res.append(solve(exp, expb, k))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
