#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# 2 1 4 7 6

# 344 12 37 60 311 613 365 328 675

def solve(arr, n):
    # the problem is asking for sum[A](k+1) = sum[A](k) + sum[A](1) where A is the set of operations performed. So the solution can be calculated easily with the broken up sum.

    # cost is only k sub-problem
    cost = 0
    max_num_seen = arr[0]
    for i in range(1, n):
        if max_num_seen > arr[i]:
            cost += max_num_seen-arr[i]
        max_num_seen = max(max_num_seen, arr[i])

    # cost is only 1 sub-problem
    max_num_seen = arr[0]
    biggest_diff = 0
    for i in range(1, n):
        diff = max_num_seen-arr[i]
        if diff > biggest_diff:
            biggest_diff = diff
        max_num_seen = max(max_num_seen, arr[i])
    cost += biggest_diff

    return cost # if the cost is k+1 per operation just solve the problem when the cost is k and 1 separately and combine the answer

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr, n))

if __name__ == "__main__":
    main()
