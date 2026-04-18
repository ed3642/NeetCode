# https://leetcode.com/problems/push-dominoes

class Solution:
    # can save some memory with 2pointer 

    def pushDominoes(self, dominoes: str) -> str:
        
        N = len(dominoes)
        positions = [('L', 0)] # stopper
        res = [token for token in dominoes]

        for i in range(N):
            if dominoes[i] == 'R':
                positions.append(('R', i))
            elif dominoes[i] == 'L':
                positions.append(('L', i))
        positions.append(('R', len(dominoes) - 1)) # stopper

        for i in range(1, len(positions)):
            # set the response from prev to current
            if positions[i - 1][0] == 'L' and positions[i][0] == 'L':
                for j in range(positions[i - 1][1], positions[i][1] + 1):
                    res[j] = 'L'
            elif positions[i - 1][0] == 'R' and positions[i][0] == 'R':
                for j in range(positions[i - 1][1], positions[i][1] + 1):
                    res[j] = 'R'
            elif positions[i - 1][0] == 'R' and positions[i][0] == 'L':
                # even or odd
                l = positions[i - 1][1]
                r = positions[i][1]
                m = (l + r) // 2
                length = r - l + 1
                if length % 2 == 0:
                    for j in range(l, m + 1):
                        res[j] = 'R'
                    for j in range(m + 1, r + 1):
                        res[j] = 'L'
                else:
                    for j in range(l, m):
                        res[j] = 'R'
                    for j in range(m + 1, r + 1):
                        res[j] = 'L'

        return ''.join(res)