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

def solve(order, n):
    seen = set()
    res = []

    for name in order[::-1]:
        if name not in seen:
            res.append(name)
            seen.add(name)

    return res

def main():

    n = rint()
    order = []
    for _ in range(n):
        order.append(rstring())
            
    print('\n'.join(map(str, solve(order, n))))

if __name__ == "__main__":
    main()
