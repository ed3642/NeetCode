class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = set([c for c in "abcdefghijklmnopqrstuvwxyz0123456789"])

        # clean the string
        s = str.lower(s)

        clean_string = []
        for c in s:
            if c in alphabet:
                clean_string.append(c)

        # two pointer method
        left = 0
        right = len(clean_string) - 1

        while left < right:
            if clean_string[left] != clean_string[right]:
                return False
            left += 1
            right -= 1

        return True
    

s = Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))