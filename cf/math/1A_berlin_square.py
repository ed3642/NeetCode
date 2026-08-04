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

def solve(n, m, a):
    x = (n+a-1)//a
    y = (m+a-1)//a
    
    return x*y

def main():
    n, m, a = read_ints()

    print(solve(n, m, a))

if __name__ == "__main__":
    main()
