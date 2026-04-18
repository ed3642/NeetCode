class Solution:
    # O (n * m)
    def removeOccurrences(self, s: str, part: str) -> str:
        
        # [daabcbaabcbc]
        # [011232112323]
        # [012]

        N = len(s)
        M = len(part)

        stack = []
        
        for c in s:          
            stack.append(c)
            if c == part[-1] and len(stack) >= M:
                i = len(stack) - 1
                is_complete = True
                for i in range(M):
                    if stack[len(stack) - 1 - i] != part[M - 1 - i]:
                        is_complete = False
                        break
                if is_complete:
                    for _ in range(M):
                        stack.pop()

        return ''.join(stack)

