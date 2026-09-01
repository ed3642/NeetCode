#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

# good problem

import sys
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr, n):
    # particles can only ever join with other particles of the same parity
    # each particle belongs to the evens or odds indexed groups

    no_positives = max(arr) # edge case, best we can do is take the max of the negatives
    if no_positives <= 0:
        return no_positives
    
    evens = 0
    odds = 0
    # we can always make a negative disappear so just take the positives of these groups
    # image these charges from parity group 1, so example evens with those charges
    # + - + => + + remove the middle and the positives combine
    # - + + => + + remove the left and the positives combine
    # + + - => + + remove the right and the positive combine
    for i in range(0, n, 2):
        if arr[i] > 0:
            evens += arr[i]
    for i in range(1, n, 2):
        if arr[i] > 0:
            odds += arr[i]

    return max(evens, odds)

def main():
    t = read_int()

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr, n))

if __name__ == "__main__":
    main()
