# https://leetcode.com/problems/maximum-distance-in-arrays/
class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        
        _min = float('inf')
        _min_2 = float('inf')
        _max = -float('inf')
        _max_2 = -float('inf')
        _min_i = 0
        _max_i = 0

        for i, arr in enumerate(arrays):
            if arr[0] < _min:
                _min, _min_2 = arr[0], _min
                _min_i = i
            elif arr[0] < _min_2:
                _min_2 = arr[0]

            if arr[-1] > _max:
                _max, _max_2 = arr[-1], _max
                _max_i = i
            elif arr[-1] > _max_2:
                _max_2 = arr[-1]

        if _min_i != _max_i:
            return _max - _min
        op1 = _max - _min_2
        op2 = _max_2 - _min

        return max(op1, op2)
    