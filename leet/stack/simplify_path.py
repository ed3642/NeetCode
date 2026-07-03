# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        s = ['/']

        if path[-1] != '/':
            path += '/'

        dirname_len = 0

        for c in path:
            if c == '/':
                if s[-1] == '/': # multiple /
                    continue
                else: # next dir
                    # /./ -> just remove /.
                    if dirname_len == 1 and s[-1] == '.': 
                        for _ in range(2):
                            s.pop()
                    # /../ -> remove /.. and then prev dir 
                    elif dirname_len == 2 and s[-1] == '.' and s[-2] == '.':
                        for _ in range(3):
                            s.pop()
                        while s and s[-1] != '/':
                            s.pop()
                        if s:
                            s.pop() # remove the prev /
                    s.append(c)
                    dirname_len = 0
            else:
                s.append(c)
                dirname_len += 1

        if len(s) > 1:
            if s[-1] == '/' or (s[-1] == '.' and s[-2] == '/'):
                s.pop()

        return ''.join(s)
