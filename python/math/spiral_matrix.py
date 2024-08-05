class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        def is_valid(i, j):
            return (
                i >= self.min_i and i <= self.max_i and
                j >= self.min_j and j <= self.max_j
            )
        
        def update_boundaries(curr_dir_index):
            if curr_dir_index == 0:
                self.min_i += 1
            elif curr_dir_index == 1:
                self.max_j -= 1
            elif curr_dir_index == 2:
                self.max_i -= 1
            elif curr_dir_index == 3:
                self.min_j += 1
        
        self.min_i = 0
        self.max_i = len(matrix) - 1
        self.min_j = 0
        self.max_j = len(matrix[0]) - 1

        curr_dir_index = 0
        # in order of transitions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        left_to_see = (self.max_i + 1) * (self.max_j + 1)
        order = []

        i = 0
        j = 0
        while left_to_see > 0:
            left_to_see -= 1
            order.append(matrix[i][j])
            n_i = i + directions[curr_dir_index][0]
            n_j = j + directions[curr_dir_index][1]
            if not is_valid(n_i, n_j):
                update_boundaries(curr_dir_index)
                curr_dir_index = (curr_dir_index + 1) % 4
                # move with valid directions
                i = i + directions[curr_dir_index][0]
                j = j + directions[curr_dir_index][1]
            else:
                i = n_i
                j = n_j
        
        return order

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
