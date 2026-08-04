#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(cards: list[list[int]], n, m):
    original_index = {}

    for i in range(n):
        cards[i].sort()
    for i in range(n):
        original_index[cards[i][0]] = i
    cards.sort(key=lambda x: x[0])

    for j in range(m):
        for i in range(1, n):
            if cards[i-1][j] > cards[i][j]:
                return [-1]

    for j in range(1, m):
        if cards[n-1][j-1] > cards[0][j]:
            return [-1]

    res = []
    for i in range(n):
        res.append(original_index[cards[i][0]]+1) # transform i into pos

    return res

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n, m = read_ints()
        cards = []
        for _ in range(n):
            cards.append(read_ints())
        print(*solve(cards, n, m))
        

if __name__ == "__main__":
    main()
