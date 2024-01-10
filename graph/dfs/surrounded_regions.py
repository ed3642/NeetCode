class Solution:
    def solve(self, board: list[list[str]]) -> None:

        def dfs(i, j, flip):
            if not isValidCoord(i, j):
                return 
            
            visited[i][j] = True

            if flip:
                board[i][j] = 'X'

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                dfs(n_i, n_j, flip)

        def isValidCoord(i, j):
            return (
                i >= 0 and i < ROWS and
                j >= 0 and j < COLS and
                board[i][j] == 'O' and
                not visited[i][j]
            )

        ROWS = len(board)
        COLS = len(board[0])

        # nothing to do in this case
        if ROWS <= 2 or COLS <= 2:
            return
        
        visited = [[False] * COLS for _ in range(ROWS)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        border = ([(i, 0) for i in range(ROWS)] + [(i, COLS - 1) for i in range(ROWS)] +
                [(0, j) for j in range(1, COLS - 1)] + [(ROWS - 1, j) for j in range(1, COLS - 1)])

        # not to be flipped
        for i, j in border:
            if board[i][j] == 'O':
                dfs(i, j, False)

        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                dfs(i, j, True)