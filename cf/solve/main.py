#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
from typing import List
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(n: int, k: int, coins: List[int]):
    
    # dp[s1][s2] = can make sum s1 and s2
    

    res = []
    

    return res

def main():
    n, k = read_ints()
    coins = read_ints()

    res = solve(n, k, coins)
    print(len(res))
    print(res)

if __name__ == "__main__":
    main()
