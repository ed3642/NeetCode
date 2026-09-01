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

def solve(arr, n, k):
    if k > n: # not enough nums
        return -1
    
    arr.sort()
    if k == 0: # all nums are bigger than 0
        return arr[0]-1 if arr[0] > 1 else -1

    if k == n:
        return arr[k-1]
    return arr[k-1] if arr[k-1] != arr[k] else -1

def main():

    n, k = rints()
    arr = rints()
            
    print(solve(arr, n, k))

if __name__ == "__main__":
    main()
