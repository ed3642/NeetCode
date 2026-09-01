#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')


def solve(string: str):
    # .....00.....11.....
    # .....11.....00..... can never remove the 11 before the 00
    
    first_11_i = string.find('11')
    last_00_i = string.rfind('00')

    if first_11_i != -1 and last_00_i != -1:
        if first_11_i < last_00_i:
            return 'NO'

    return 'YES'

def main():
    t = read_int()

    for _ in range(t):
        string = read_string()
        print(solve(string))

if __name__ == "__main__":
    main()
