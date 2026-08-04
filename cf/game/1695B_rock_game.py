#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr, n):
    if n % 2 != 0: # mike always wins if odd num piles, he can just empty the first pile and will land on it
        return 'Mike'

    # if even piles each players piles never mix so each player has a set of piles, the player with the smallest pile in their set loses since that pile will run out first.
    min_pile_i = 0
    for i in range(n):
        if arr[i] < arr[min_pile_i]:
            min_pile_i = i

    if min_pile_i % 2 == 0: # min pile belongs to Mike
        return 'Joe'
    return 'Mike'

def main():
    t = read_int()

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr, n))

if __name__ == "__main__":
    main()
