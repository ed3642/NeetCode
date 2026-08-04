#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import deque
import sys
input = sys.stdin.readline

def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))
def read_chars(): return list(input().strip())
def read_int_iter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

# O(n)
def solve(n, g):
    res = [0] * n
    is_tree_node = [False] * (n+1)
    abs_leaf_node = [False] * (n+1)
    indeg = [0] * (n+1)

    for i in range(n):
        node = g[i]
        indeg[node] += 1

    q = deque()

    # determine type for each node
    for node in range(1, n+1):
        if indeg[node] == 0:
            q.append(node)
            abs_leaf_node[node] = True

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            is_tree_node[node] = True
            nei = g[node-1]
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)

    # record answers
    for i in range(n):
        node = i+1
        if not is_tree_node[node]: # aka it must be a cycle_node
            res[i] = node # answer is just itself
        elif abs_leaf_node[node]:
            # answer is the first cycle node that this tree lands on
            landing = node
            while is_tree_node[landing]:
                if res[landing-1] != 0: # this tree has already computed the final landing
                    landing = res[landing-1]
                    break
                landing = g[landing-1]
            # all nodes on this tree have the same answer
            res[i] = landing # mark the leaf
            node = g[i] # start at the leaf nei
            while is_tree_node[node]:
                if res[node-1] != 0:
                    break # path res already recorded
                res[node-1] = landing
                node = g[node-1]

    return res

# O(n^2)
def solve(n, g):
    res = [0] * n

    for i in range(n):
        visited = [False] * (n+1)
        node = i+1
        visited[node] = True
        while True:
            node = g[node-1]
            if visited[node]:
                res[i] = node
                break
            visited[node] = True

    return res

def main():
    n = read_int()

    print(*solve(n, read_ints()))

if __name__ == "__main__":
    main()
