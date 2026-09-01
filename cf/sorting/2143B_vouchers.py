#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(prices: list[int], vou: list[int]):
    N = len(prices)
    prices.sort(reverse=True)
    vou.sort()

    c = 0
    i = 0
    for v in vou:
        for _ in range(v-1):
            c += prices[i]
            i += 1
            if i >= N: # didnt need all vouchers
                return c
        # free one from this voucher
        i += 1
        if i >= N: # done all items
            return c
    
    for j in range(i, len(prices)):
        c += prices[j]

    return c

def main():
    t = read_int()

    for _ in range(t):
        n, m = read_ints()
        prices = read_ints()
        vou = read_ints()
        print(solve(prices, vou))

if __name__ == "__main__":
    main()
