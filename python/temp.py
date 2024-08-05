class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        seen = set()
        unique = set()

        for c in arr:
            if c not in seen:
                seen.add(c)
                unique.add(c)
            elif c in unique:
                unique.remove(c)

        unique_order_pos = 0
        for c in arr:
            if c in unique:
                unique_order_pos += 1
            if unique_order_pos == k:
                return c
            elif unique_order_pos >= len(unique):
                return ''
        
        return ''