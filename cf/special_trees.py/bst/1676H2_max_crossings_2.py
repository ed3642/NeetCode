#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from typing import List

class FenwickTree:
    # sum fenwick tree
    # elems must be 0 indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (self.n+1)

    def query(self, i):
        sum = 0
        while i > 0:
            sum += self.tree[i]
            i -= i & -i
        return sum

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    
    # inclusive l and r
    def range_query(self, l, r):
        return self.query(r)  - self.query(l-1)

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr: list[int], n):
    # for ith wire: num wires that start before it and land after or eq to it
    res = 0

    bst = FenwickTree(n)

    for i in range(n):
        end = arr[i]
        tree_index = end
        wires_ending_after_eq = bst.range_query(tree_index, n)
        res += wires_ending_after_eq
        bst.update(tree_index, 1)

    return res

def main():
    t = read_int()

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        print(solve(arr, n))

if __name__ == "__main__":
    main()
