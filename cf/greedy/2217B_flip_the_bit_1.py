#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

INF = float('inf')
def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# in this version of the problem, k indices is always len 1

def solve(bits, k):
    # l     k r
    # 0 1 0 1 0 1

    # l 2 x   k                 x 2 r  
    # 0 1 1 0 1 1 0 1 0 0 1 0 1 0 1 0 1
    # l     k                 r
    # 0 1 0 1 0 1 0 1 0 1 0 1 0 1
    # 3 9

    # has to be even num flips since k always has to flip back to original
    
    N = len(bits)
    k -= 1 # make 0 indexed
    special = bits[k]

    rbits = [bits[0]] # reduced bits

    for i in range(1, k):
        if bits[i] != bits[i-1]:
            rbits.append(bits[i])
    if k != 0:
        rbits.append(bits[k])
    temp = len(rbits)-1 # new k index
    for i in range(k+1, N):
        if bits[i] != bits[i-1]:
            rbits.append(bits[i])
    k = temp

    M = len(rbits)
    l = -INF
    r = INF

    for i in range(k):
        if rbits[i] != special:
            l = i
            break
    for i in range(M-1, k, -1):
        if rbits[i] != special:
            r = i
            break

    flips_l = k-l if l != -INF else 0
    flips_r = r-k if r != INF else 0
    total = max(flips_l, flips_r)
    total = total if total%2 == 0 else total+1

    return total

def main():
    t = read_int()

    for _ in range(t):
        n, _ = read_ints()
        bits = read_ints()
        k = read_int()
        print(solve(bits, k))

if __name__ == "__main__":
    main()
