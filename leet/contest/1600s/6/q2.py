class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        
        arr = [1] * n

        for _ in range(1, k + 1):
            for i in range(1, n):
                arr[i] += arr[i - 1]
        
        return arr[-1] % (10**9 + 7)
    
s = Solution()
print(s.valueAfterKSeconds(3, 5))