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

def solve(s, t):
    return 'YES' if len(set(s) & set(t)) > 0 else 'NO'

def main():
    t = read_int()

    res = []
    for _ in range(t):
        s = read_string()
        t = read_string()
        res.append(solve(s, t))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
