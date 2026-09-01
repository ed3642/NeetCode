#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

MOD = 10**9+7
INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(edges, n, queries, m):
    # standard cf approach to deal with trees is to see we dont dfs into the parent of u
    # New semantics: calls node u, parent p, and nei v.

    # root at 1
    al = [[] for _ in range(n+1)]
    leafs = [0] * (n+1)
    res = [0] * m

    for u, v in edges:
        al[u].append(v)
        al[v].append(u)

    # dfs(1, 0) => for CF need to do dfs on trees iteratively

    s = deque([(1, 0)])
    order = []
    while s:
        u, p = s.popleft()
        order.append((u, p))

        for v in al[u]:
            if v != p:
                s.append((v, u))

    # go through the order in reverse to simulate the postfix dfs
    for u, p in order[::-1]:
        if u != 1 and len(al[u]) == 1: # isleaf
            leafs[u] = 1
            continue

        for v in al[u]:
            if v != p:
                leafs[u] += leafs[v]

    for i, (a, b) in enumerate(queries):
        res[i] = leafs[a]*leafs[b]

    return res

def main():

    t = rint()
    for _ in range(t):
        n = rint()
        e = []
        for _ in range(n-1):
            e.append(rints())
        m = rint()
        q = []
        for _ in range(m):
            q.append(rints())
        print('\n'.join(map(str, solve(e, n, q, m))))

if __name__ == "__main__":
    main()
