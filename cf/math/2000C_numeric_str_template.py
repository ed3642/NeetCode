#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import defaultdict
import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(arr, strings, m):
    res = ['YES'] * m

    for i in range(m):
        c_to_num_map = defaultdict(int)
        num_to_c_map = defaultdict(int)

        if len(strings[i]) != len(arr):
            res[i] = 'NO'
            continue

        for j, c in enumerate(strings[i]):
            number = arr[j]
            if c in c_to_num_map and c_to_num_map[c] != number:
                res[i] = 'NO'
                break
            if number in num_to_c_map and num_to_c_map[number] != c:
                res[i] = 'NO'
                break
            c_to_num_map[c] = number
            num_to_c_map[number] = c

    return res

def main():
    line = input().strip()
    t = int(line) if line else 1

    for _ in range(t):
        n = read_int()
        arr = read_ints()
        m = read_int()
        strings = []
        for _ in range(m):
            strings.append(read_chars())
        res = solve(arr, strings, m)
        for out in res:
            print(out)

if __name__ == "__main__":
    main()
