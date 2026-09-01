#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from bisect import bisect_left
import sys
input = sys.stdin.readline

INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(worms, jworms):
    # 2 7 3  4  9
    # 2 9 12 16 25
    N = len(worms)
    M = len(jworms)
    res = [0] * M

    for i in range(1, N):
        worms[i] += worms[i-1]

    for q in range(M):
        res[q] = bisect_left(worms, jworms[q])+1 # want 1 indexed

    return res

def main():
    n = rint()
    worms = rints()
    m = rint()
    jworms = rints()

    print('\n'.join(map(str, solve(worms, jworms))))

if __name__ == "__main__":
    main()
