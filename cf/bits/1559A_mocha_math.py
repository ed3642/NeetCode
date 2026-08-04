# https://codeforces.com/problemset/problem/1559/A

#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(n, data):
    biggest = max(data)
    for num in data:
        biggest &= num
    return biggest

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n = read_int()
        data = read_ints()
        ans = solve(n, data)
        if ans is not None:
            print(ans)

if __name__ == "__main__":
    main()
