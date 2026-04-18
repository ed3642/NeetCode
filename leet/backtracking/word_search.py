# https://leetcode.com/problems/word-search
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def bt(i, j, word_i, explored: set):
            if board[i][j] != word[word_i]:
                return False
            if board[i][j] == word[word_i] and word_i == len(word) - 1:
                return True
            
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and (n_i, n_j) not in explored:
                    explored.add((n_i, n_j))
                    if bt(n_i, n_j, word_i + 1, explored):
                        return True
                    explored.remove((n_i, n_j))
            return False

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        I_BOUND = len(board)
        J_BOUND = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Prune 1: start from the least frequent letter word[0] or word[-1]
        start_freq = 0
        end_freq = 0
        for i in range(I_BOUND):
            for j in range(J_BOUND):
                if board[i][j] == word[0]:
                    start_freq += 1
                if board[i][j] == word[-1]:
                    end_freq += 1
        # other optimizations
        # 1. Check if any letter in word appears more times than in board (early exit if insufficient letters).
        # 2. Precompute frequencies of each letter in board and reorder word to start from the least frequent character among all letters, not just first or last.
        # 3. Track visited counts per letter to quickly abandon paths that exceed available frequency.       
        
        if start_freq > end_freq:
            word = word[::-1]

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                if board[i][j] == word[0] and bt(i, j, 0, set([(i, j)])):
                    return True
        return False
    
    # start at each letter explore each neighbour
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(target_i, i, j, visited):
            if target_i == len(word):
                return True
            
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            for di, dj in directions:
                next_i = i + di
                next_j = j + dj
                if (isValidCoord(next_i, next_j) and 
                    (next_i, next_j) not in visited and
                    board[next_i][next_j] == word[target_i]):
                    visited.add((next_i, next_j))
                    if backtrack(target_i + 1, next_i, next_j, visited):
                        return True
                    visited.remove((next_i, next_j))

        def isValidCoord(i, j):
            return (i >= 0 and i < len(board)
                and j >= 0 and j < len(board[0]))
        
        # get least freq end
        freq = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                freq[board[i][j]] += 1
        
        if freq[word[0]] > freq[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(1, i, j, {(i, j)}):
                        return True
        return False
