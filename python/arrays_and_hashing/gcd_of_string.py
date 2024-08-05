class Solution:
    # nice solution
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def check(candidate, string):
            # see if it can build string
            i = 0
            for ch in string:
                if candidate[i] != ch:
                    return False
                i += 1
                if i >= len(candidate):
                    i = 0
            return True


        # longest on str1
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        for i in range(len(str2), 0, -1):
            candidate = str2[:i]
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                if check(candidate, str2) and check(candidate, str1):
                    return candidate
        
        return ''