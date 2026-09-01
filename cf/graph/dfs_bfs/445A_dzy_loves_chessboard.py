#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from collections import deque
import sys
input = sys.stdin.readline

MOD = 10**9+7
INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(board, n, m):

    def isin(i, j):
        return 0 <= i < n and 0 <= j < m

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(0, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    BAD = '-'

    status = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()

            if board[i][j] != BAD:
                if status == 0:
                    board[i][j] = 'B'
                else:
                    board[i][j] = 'W'

            for di, dj in directions:
                ni = i+di
                nj = j+dj
                if isin(ni, nj) and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = True
        status ^= 1

    for i in range(n):
        board[i] = ''.join(board[i])

    return board

def main():

    n, m = rints()
    board = []
    for _ in range(n):
        board.append(rchars())

    print('\n'.join(map(str, solve(board, n, m))))

if __name__ == "__main__":
    main()
