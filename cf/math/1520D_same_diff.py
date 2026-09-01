#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import defaultdict
import sys
input = sys.stdin.readline

INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr):
    # rewrite the equality were looking for and the problem become much simpler 
    # aj - ai = j - i
    # aj - j = ai - i
    # 3 5  1 4 6 6
    # 3 4 -1 1 2 1

    N = len(arr)
    c = 0

    diffc = defaultdict(int)

    for i in range(N):
        diffc[arr[i]-i] += 1

    for d in diffc:
        x = diffc[d]-1
        c += (x*(x+1))//2

    return c

def main():
    res = []

    t = rint()
    for _ in range(t):
        n = rint()
        arr = rints()
        res.append(solve(arr))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
