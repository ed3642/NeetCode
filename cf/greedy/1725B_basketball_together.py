#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(n, enemy_p, arr: list[int]):
    arr.sort()
    teams = 0

    l = -1
    for r in range(n-1, -1, -1):
        p = arr[r]
        players_needed = (enemy_p)//p # original formula is (enemy_p+p-p-1)//p but after simplifying and +1 to make it strictly greater than, that is what is left
        l += players_needed
        if l >= r:
            return teams
        teams += 1
    return teams

def main():
    n, p = read_ints()
    arr = read_ints()

    print(solve(n, p, arr))

if __name__ == "__main__":
    main()
