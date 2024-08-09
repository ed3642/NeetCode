# https://leetcode.com/problems/generate-parentheses
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def backtrack(left_count, right_count, builder: list):
            if left_count == right_count and left_count == n:
                res.append(''.join(builder))
                return None
        
            if left_count < n:
                builder.append('(')
                backtrack(left_count + 1, right_count, builder)
                builder.pop()
            if right_count < n and left_count > right_count:
                builder.append(')')
                backtrack(left_count, right_count + 1, builder)
                builder.pop()


        res = []
        backtrack(0, 0, [])
        return res

    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(string, left_backets, right_backets):
            if len(string) == n * 2:
                solutions.append(string)
                return
            
            # explore solutions
            if right_backets <= left_backets:
                if left_backets < n:
                    backtrack(string + '(', left_backets + 1, right_backets)
                if right_backets < n:
                    backtrack(string + ')', left_backets, right_backets + 1)

        solutions = []
        backtrack('', 0, 0)
        return solutions
    
    def generateParenthesis2(self, n: int) -> list[str]:
        def backtrack(builder, lefts, rights):
            if lefts == n and rights == n:
                res.append(''.join(builder))
                return
            
            if lefts < n:
                builder.append('(')
                backtrack(builder, lefts + 1, rights)
                builder.pop()
            if rights < n and rights < lefts:
                builder.append(')')
                backtrack(builder, lefts, rights + 1)
                builder.pop()
                
        res = []
        backtrack([], 0, 0)
        return res

    # iterative solution
    # imitating recursion with a stack
    def generateParenthesis2(n):
        stack = [] # (string, num_left_brackets, num_right_brackets)
        stack.append(('(', 1, 0))
        solutions = []

        while stack:
            string, num_left_brackets, num_right_brackets = stack.pop()
            
            if len(string) == n * 2:
                solutions.append(string)
            elif num_right_brackets <= num_left_brackets:
                if num_left_brackets < n:
                    stack.append((string + '(', num_left_brackets + 1, num_right_brackets))
                if num_right_brackets < n:
                    stack.append((string + ')', num_left_brackets, num_right_brackets + 1))
                    
        return solutions



# backtracking template
# def backtrack(candidate):
#     if find_solution(candidate):
#         output(candidate)
#         return
    
#     # iterate all possible candidates.
#     for next_candidate in list_of_candidates:
#         if is_valid(next_candidate):
#             # try this partial candidate solution
#             place(next_candidate)
#             # given the candidate, explore further.
#             backtrack(next_candidate)
#             # backtrack
#             remove(next_candidate)