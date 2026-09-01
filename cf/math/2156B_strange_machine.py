#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

# key presprectives from this problem. 1. try to see the expensive calculations and how to mitigate them. 2. 2**x is very slow for large x, can be compared to O(x)

import sys
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(types: str, queries):
    N = len(queries)
    M = len(types)

    type_b_present = types.find('B') >= 0
    if not type_b_present:
        # were just doing subtraction by 1 each time
        return queries

    compressed_types = []

    seq_len = 1
    for i in range(M-1):
        if types[i] != types[i+1]:
            compressed_types.append([seq_len, types[i]])
            seq_len = 1
        else:
            seq_len += 1

    compressed_types.append([seq_len, types[M-1]])
    L = len(compressed_types)

    for i in range(N):
        q = queries[i]
        s = 0
        j = 0
        while q > 0:
            if compressed_types[j][1] == 'A':
                q -= compressed_types[j][0]
                overshot = q if q < 0 else 0
                s = s+compressed_types[j][0]+overshot
            else:
                for _ in range(compressed_types[j][0]):
                    q //= 2
                    s += 1
                    if q == 0:
                        break
            j = (j+1) % L
        queries[i] = s

    return queries

def main():
    t = read_int()

    for _ in range(t):
        n, m = read_ints()
        types = read_string()
        queries = read_ints()
        res = solve(types, queries)
        for r in res:
            print(r)

if __name__ == "__main__":
    main()
