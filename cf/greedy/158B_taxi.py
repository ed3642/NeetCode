#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
from collections import Counter
input = sys.stdin.readline

INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')


def solve(arr):
    # 1 1 1 2 2 3 3 3 3 3 3
    # 2 2 2 3 3 3 3
    # 1 2

    # 2 -> 2 | 1 1

    N = len(arr)
    hz = Counter(arr)

    # optimal 4s
    cars = hz[4]    
    # optimal 3s with 1s
    min_3_1 = min(hz[3], hz[1])
    cars += min_3_1
    hz[3] -= min_3_1
    hz[1] -= min_3_1
    # optimal 2s with 2s
    two_pairs = hz[2]//2
    cars += two_pairs
    hz[2] -= two_pairs*2
    # optimal 2s with 2 1s
    one_pairs = hz[1]//2
    min_2_1p = min(one_pairs, hz[2])
    cars += min_2_1p
    hz[2] -= min_2_1p
    hz[1] -= min_2_1p*2
    # optimal left over 2s with 1s
    min_2_1 = min(hz[2], hz[1])
    cars += min_2_1
    hz[2] -= min_2_1
    hz[1] -= min_2_1
    # optimal 1s
    round_up_1 = ((hz[1]+3)//4)
    cars += round_up_1
    # left over groups
    cars += hz[3]+hz[2]

    return cars

def main():
    res = []

    n = rint()
    arr = rints()

    res.append(solve(arr))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
