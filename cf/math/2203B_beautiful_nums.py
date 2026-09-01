#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import defaultdict
import sys
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# fx ffx
# 0 0
# 1 1
# 2 2 
# 3 3
# 4 4
# 5 5
# 6 6
# 7 7
# 8 8
# 9 9
# 10 1 breaks

def solve(n):
    # min digits to change to get the sum < 10
    # no trailing 0s (just cant change the first digit to a 0)


    hz = defaultdict(int)
    _sum = 0
    rm = 9
    c = 0

    # digits past the first one
    while n >= 10:
        d = n%10
        _sum += d
        hz[d] += 1
        n //= 10
    _sum += n # first digit
    hz[n-1] += 1 # first digit can go down to 1 only

    while _sum >= 10 and rm > 0:
        while rm > 0 and hz[rm] == 0:
            rm -= 1
        _sum -= rm
        hz[rm] -= 1
        c += 1

    return c

def main():
    t = read_int()

    res = []
    for _ in range(t):
        res.append(solve(read_int()))

    print('\n'.join(map(str, res)))
        
if __name__ == "__main__":
    main()
