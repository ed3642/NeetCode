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

def solve(b, g, n, m):

    b.sort()
    g.sort()
    c = 0

    i = 0
    j = 0
    while i < n and j < m:
        if abs(b[i]-g[j]) <= 1:
            i += 1
            j += 1
            c += 1
        elif g[j] > b[i]: # boy cant be matched
            i += 1
        else: # girl cant be matched
            j += 1

    return c

def main():

    n = rint()
    boys = rints()
    m = rint()
    girls = rints()
            
    print(solve(boys, girls, n, m))

if __name__ == "__main__":
    main()
