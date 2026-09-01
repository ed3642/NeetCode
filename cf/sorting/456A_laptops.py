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

def solve(laptops):
    N = len(laptops)
    laptops.sort(key=lambda x: x[0])

    for i in range(1, N):
        if laptops[i-1][1] > laptops[i][1]:
            return 'Happy Alex'
    return 'Poor Alex'

def main():

    n = rint()
    prices = [0] * n
    qualities = [0] * n

    for i in range(n):
        prices[i], qualities[i] = rints()
    
    print(solve(list(zip(prices, qualities))))

if __name__ == "__main__":
    main()
