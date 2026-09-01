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

def solve(arr, l):
    arr.sort()
    arr.append(l+(l-arr[-1])) # to mirror the last pole about l

    max_dist = (arr[0]-(-arr[0])) # to mirror the first pole about 0
    for i in range(1, len(arr)):
        max_dist = max(max_dist, arr[i]-arr[i-1])

    return max_dist/2

def main():
    res = []

    n, l = rints()
    arr = rints()

    print(solve(arr, l))

if __name__ == "__main__":
    main()
