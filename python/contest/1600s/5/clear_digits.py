class Solution:
    def clearDigits(self, s: str) -> str:
        
        last_non_digit = [] # stack
        to_delete = set()

        for i, ch in enumerate(s):
            if ch.isalpha():
                last_non_digit.append(i)
            elif ch.isdigit():
                to_delete.add(i)
                if last_non_digit:
                    to_delete.add(last_non_digit.pop())
        
        res = []
        for i, ch in enumerate(s):
            if i not in to_delete:
                res.append(ch)
        
        return ''.join(res)
    
s = Solution()
print(s.clearDigits("cb34"))