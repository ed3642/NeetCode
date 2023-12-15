from collections import defaultdict


class Solution:
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
