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

def solve(n, k):
    return (k+n-1)//n

def main():

    n, k = read_ints()
    print(solve(n, k))

if __name__ == "__main__":
    main()
