# https://codeforces.com/problemset/problem/709/A

#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(data, prf, pof, n):
    a, b = data
    a -= 1
    b -= 1
    if a < b:
        return prf[b]-prf[a] if a >= 0 else prf[b]
    else:
        return pof[b]-pof[a] if a <= n-1 else pof[b]

def main():
    n, m = read_ints()
    arr = read_ints()

    # damage prefix and postfix
    prf = [0] * n
    pof = [0] * n
    
    for i in range(1, n):
        dmg = arr[i-1]-arr[i]
        if dmg > 0:
            prf[i] = dmg
        prf[i] += prf[i-1]
    
    for i in range(n-2, -1, -1):
        dmg = arr[i+1]-arr[i]
        if dmg > 0:
            pof[i] = dmg
        pof[i] += pof[i+1]

    for _ in range(m):
        print(solve(read_ints(), prf, pof, n))

if __name__ == "__main__":
    main()
