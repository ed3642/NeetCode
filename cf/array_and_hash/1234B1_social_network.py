#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import deque
import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_string(): return input().strip()
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(msgs, n, k):
    q = deque()
    inq = set()

    for m in msgs:
        if len(q) < k:
            if m not in inq:
                q.append(m)
                inq.add(m)
        else:
            if m not in inq:
                removed = q.popleft()
                inq.remove(removed)
                q.append(m)
                inq.add(m)

    return list(reversed(q))

def main():
    n, k = read_ints()
    arr = read_ints()
    res = solve(arr, n, k)
    print(len(res))
    print(*res)

if __name__ == "__main__":
    main()
