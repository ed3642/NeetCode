class Solution:
    # theres a far better way of doing this
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # return elem thats closer
        def getCloser(a, b):
            if not isValid(a):
                return b
            if not isValid(b):
                return a
            if abs(arr[a] - x) < abs(arr[b] - x):
                return a
            elif abs(arr[a] - x) > abs(arr[b] - x):
                return b
            else:
                return min(a, b)
        
        def isValid(index):
            return (
                index >= 0 and index < len(arr)
            )
        
        if len(arr) <= 1:
            return arr if k == 1 else []

        l = 0
        r = len(arr) - 1
        m = -1
        closest_i = -1
        while l + 1 < r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m
            elif arr[m] > x:
                r = m
            else:
                closest_i = m
                break
        
        # get closest index
        if closest_i == -1:
            closest_i = getCloser(l, r)
            
        # expand to closest elems
        k -= 1 # we added closests_i already accounted for
        a = closest_i - 1
        b = closest_i + 1
        start = closest_i
        end = closest_i
        while k > 0:
            closer = getCloser(a, b)
            if closer == a:
                start = a
                a -= 1
            else:
                end = b
                b += 1
            k -= 1

        return arr[start:end + 1]

s = Solution()
print(s.findClosestElements([1,2,3,4,4,4,4,5,5], 3, 3))