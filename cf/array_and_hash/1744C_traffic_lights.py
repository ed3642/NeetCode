#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(n, c, pattern: list):
    if c == 'g':
        return 0
    
    max_distance_to_g = 0
    first_g_i = pattern.index('g')

    for i in range(first_g_i, -1, -1):
        if pattern[i] == c:
            max_distance_to_g = max(max_distance_to_g, first_g_i-i)

    last_g_i = n+first_g_i
    for i in range(n-1, first_g_i, -1):
        if pattern[i] == c:
            max_distance_to_g = max(max_distance_to_g, last_g_i-i)
        elif pattern[i] == 'g':
            last_g_i = i
    return max_distance_to_g

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n, c = input().split(' ')
        c = c.strip()
        string = read_chars()
        ans = solve(int(n), c, string)
        if ans is not None:
            print(ans)

if __name__ == "__main__":
    main()
