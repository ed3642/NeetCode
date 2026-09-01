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

def solve(arr, n):
    # 1 4 3 7 10
    # a&b >= a^b
    # if the leftmost bit is 1 for both pairs then a&b is greater or eq, otherwise a^b is greater
    # since 10000... is bigger than 01111... for bitstrings of the same length

    c = 0
    hz = defaultdict(int)

    for i in range(n):
        hz[arr[i].bit_length()] += 1

    for size in hz:
        m = hz[size]-1
        c += (m*(m+1))//2

    return c

def main():
    res = []

    t = rint()
    for _ in range(t):
        n = rint()
        arr = rints()
        res.append(solve(arr, n))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
