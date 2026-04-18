# https://leetcode.com/contest/warm-up-contest

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        stack = []
        N = len(input)
        i = 0
        curr_len = 0
        curr_file_len = 0
        
        while i < N:
            if input[i] == '\n':
                stack.append(curr_len)
                curr_file_len += curr_len
                curr_len = 0
                i += 1
                if input[i] == '\t':
                    # its a sub dir
                    depth = 0
                    while i < N and input[i] == '\t':
                        i += 1
                        depth += 1
                    # pop the stack until were at the right level
                    while len(stack) > depth:
                        curr_file_len -= stack.pop()
                else:
                    # its a new root dir
                    stack.clear()
                    curr_file_len = 0
                    curr_len = 0
            elif input[i] == '.':
                i += 1
                curr_len += 1
                while i < N and input[i] != '\n':
                    # its a file, get the whole extention
                    i += 1
                    curr_len += 1
                cand_len = curr_file_len + curr_len + len(stack) # +1 for each / in the path
                max_len = max(cand_len, max_len)
            else:
                curr_len += 1
                i += 1

        return max_len

s = Solution()
print(s.lengthLongestPath("a.txt\nb.txt")) # 5
print(s.lengthLongestPath("a.txt\nb.txt\nlong.txt")) # 8

print(s.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt")) # 12
print(s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))