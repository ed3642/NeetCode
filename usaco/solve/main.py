#!/usr/bin/env python3
# PowerShell:  python main.py

import sys
from typing import List
sys.stdin = open("factory.in", "r")
sys.stdout = open("factory.out", "w")
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def read_input():
    return read_ints()

def solve(g: List[List[int]], n: int):
    
    def dfs(node, visited):
        visited[node] = True
        for nei in g[node]:
            if not visited[nei]:
                dfs(nei, visited)
    
    can_visit = [[] for _ in range(n + 1)]
    for node in range(1, n + 1):
        visited = [False] * (n + 1)
        dfs(node, visited)
        can_visit[node] = visited
    
    # check first node that can be visited by all
    for cand_node in range(1, n + 1):
        valid = True
        for node in range(1, n + 1):
            if cand_node != node:
                if not can_visit[node][cand_node]:
                    valid = False
                    break
        if valid:
            return cand_node

    return -1

def main():
    n = read_int()
    
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        f, t = read_input()
        g[f].append(t)
    res = solve(g, n)
    if res:
        print(res)

if __name__ == "__main__":
    main()
