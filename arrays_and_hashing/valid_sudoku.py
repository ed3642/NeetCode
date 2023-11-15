class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hs = set()
        N = len(board)

        # each row
        for row in board:
            hs.clear()
            for n in row: 
                if n != '.' and not n in hs:
                    hs.add(n)
                elif n in hs:
                    return False
        
        # each column
        for i in range(N):
            hs.clear()
            for j in range(N):
                n = board[j][i]
                if n != '.' and not n in hs:
                    hs.add(n)
                elif n in hs:
                    return False
                
        # each square
        for i in range(N):
            hs.clear()
            for j in range(N):
                n = board[(j // 3) + ((i // 3) * 3)][((j % 3) + (i * 3)) % 9]
                if n != '.' and not n in hs:
                    hs.add(n)
                elif n in hs:
                    return False
        
        return True

s = Solution()

input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s.isValidSudoku(input)