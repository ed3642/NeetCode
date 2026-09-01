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

def solve(data):
    ...

def main():
    res = []

    t = rint()
    for _ in range(t):
        data = read_all()
        ans = solve(data)
        if ans is not None:
            res.append(ans)
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
