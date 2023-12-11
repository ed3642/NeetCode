class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        def traverse(i, j, direction: str): # directions: l,r,u,d
            if direction == 'l':
                return (i, j - 1)
            elif direction == 'r':
                return (i, j + 1)
            elif direction == 'u':
                return (i - 1, j)
            elif direction == 'd':
                return (i + 1, j)
        
        def isValidPos(i, j, bounds):
            return (i > bounds[0] and i < bounds[1] and
                j > bounds[2] and j < bounds[3])
        
        res = []
        dir = 'r' # starting direction
        i = 0
        j = 0
        top_bound = -1
        bottom_bound = len(matrix)
        left_bound = -1
        right_bound = len(matrix[0])
        while len(res) < len(matrix) * len(matrix[0]):
            if isValidPos(i, j, [top_bound, bottom_bound, left_bound, right_bound]):
                res.append(matrix[i][j])
                temp_i, temp_j = traverse(i, j, dir)
                if isValidPos(temp_i, temp_j, [top_bound, bottom_bound, left_bound, right_bound]):
                    i, j = temp_i, temp_j
                else:
                    # next direction
                    if dir == 'l':
                        bottom_bound -= 1
                        dir = 'u'
                    elif dir == 'r':
                        top_bound += 1
                        dir = 'd'
                    elif dir == 'u':
                        left_bound += 1
                        dir = 'r'
                    elif dir == 'd':
                        right_bound -= 1
                        dir = 'l'
                    i, j = traverse(i, j, dir) # step into valid area
        
        return res
