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

def solve(readings, n):

    n = len(readings)

    for i in range(1, n):
        if (readings[i][0] < readings[i-1][0]) or (readings[i][1] < readings[i-1][1]) or (readings[i][1]-readings[i-1][1] > readings[i][0]-readings[i-1][0]):
            return 'NO'
    return 'YES'

def main():
    res = []

    t = rint()
    for _ in range(t):
        n = rint()
        readings = [[0, 0]]
        for _ in range(n):
            readings.append(rints())
        res.append(solve(readings, n))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
