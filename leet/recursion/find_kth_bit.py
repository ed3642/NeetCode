# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        if n == 1:
            return '0'
        
        length = (1 << n) - 1
        m = length // 2
        k_i = k - 1 # k by index

        if k_i == m:
            return '1'
        elif k_i < m:
            return self.findKthBit(n - 1, k)
        else:
            return '1' if self.findKthBit(n - 1, length - k + 1) == '0' else '0'
  
    def findKthBit(self, n: int, k: int) -> str:
        
        def gen_string(n):
            if n == 1:
                return '0'
            
            prev = gen_string(n - 1)
            return prev + '1' + invert(prev)[::-1]
        
        def invert(string):
            bits = [int(bit) for bit in string]
            return ''.join(map(lambda x: str(x ^ 1), bits))
        
        return gen_string(n)[k - 1]