# https://leetcode.com/problems/number-of-paths-with-max-score

from collections import defaultdict
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        MOD = 10**9+7
        INF = float('inf')
        N = len(board)
        M = len(board[0])

        # num paths to make biggest sum possible to this cell, [biggest sum, paths]
        dp = [[[-INF, 0] for _ in range(M)] for _ in range(N)]
        dp[N-1][M-1] = [0, 1]

        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                if i == N-1 and j == M-1:
                    continue
                board_val = board[i][j]
                if board_val != 'X':
                    val = int(board_val) if board_val != 'E' else 0
                    right = dp[i][j+1][0] if j < M-1 else -INF
                    bot = dp[i+1][j][0] if i < N-1 else -INF
                    rb = dp[i+1][j+1][0] if (i < N-1 and j < M-1) else -INF
                    max_option = max(right, bot, rb)
                    if max_option == -INF:
                        continue
                    dp[i][j][0] = max_option+val
                    if right == max_option:
                        dp[i][j][1] = (dp[i][j][1]+dp[i][j+1][1]) % MOD
                    if bot == max_option:
                        dp[i][j][1] = (dp[i][j][1]+dp[i+1][j][1]) % MOD
                    if rb == max_option:
                        dp[i][j][1] = (dp[i][j][1]+dp[i+1][j+1][1]) % MOD

        # no path to E, return [0, 0]
        if dp[0][0][1] == 0:
            return [0, 0]
        return dp[0][0]

    # TLE
    def pathsWithMaxScore2(self, board: List[str]) -> List[int]:
        
        MOD = 10**9+7

        N = len(board)
        M = len(board[0])

        dp = [[defaultdict(int) for _ in range(M)] for _ in range(N)]
        dp[N-1][M-1][0] = 1

        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                if i == 0 and j == 0:
                    continue
                for s in dp[i][j]:
                    if i > 0 and j > 0:
                        val_upleft = board[i-1][j-1]
                        if val_upleft.isnumeric():
                            dp[i-1][j-1][s+int(val_upleft)] = (dp[i-1][j-1][s+int(val_upleft)]+dp[i][j][s]) % MOD
                    if i > 0:
                        val_up = board[i-1][j]
                        if val_up.isnumeric():
                            dp[i-1][j][s+int(val_up)] = (dp[i-1][j][s+int(val_up)]+dp[i][j][s]) % MOD
                    if j > 0:
                        val_left = board[i][j-1]
                        if val_left.isnumeric():
                            dp[i][j-1][s+int(val_left)] = (dp[i][j-1][s+int(val_left)]+dp[i][j][s]) % MOD

        max_sum = 0
        if len(dp[1][1]) > 0:
            max_sum = max(dp[1][1].keys())
        if len(dp[0][1]) > 0:
            max_sum = max(max_sum, *dp[0][1].keys())
        if len(dp[1][0]) > 0:
            max_sum = max(max_sum, *dp[1][0].keys())

        return [max_sum, (dp[1][1][max_sum]+dp[0][1][max_sum]+dp[1][0][max_sum]) % MOD]
        
    