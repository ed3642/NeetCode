#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# O(distance)
def solve(s, d):
    c, r = s[0], int(s[1])
    dc, dr = d[0], int(d[1])
    path = []

    tr = {chr(ord('a')+i): chr(ord('a')+i+1) for i in range(7)}
    tl = {chr(ord('a')+i): chr(ord('a')+i-1) for i in range(1, 8)}

    while c != dc or r != dr:
        if c < dc and r < dr:
            path.append('RU')
            c = tr[c]
            r += 1
        elif c < dc and r > dr:
            path.append('RD')
            c = tr[c]
            r -= 1
        elif c > dc and r < dr:
            path.append('LU')
            c = tl[c]
            r += 1
        elif c > dc and r > dr:
            path.append('LD')
            c = tl[c]
            r -= 1
        elif c < dc:
            path.append('R')
            c = tr[c]
        elif c > dc:
            path.append('L')
            c = tl[c]
        elif r < dr:
            path.append('U')
            r += 1
        else:
            path.append('D')
            r -= 1

    return (len(path), path)

def main():
    s = read_chars()
    d = read_chars()

    length, path = solve(s, d)
    print(length)
    for p in path:
        print(p)

if __name__ == "__main__":
    main()
