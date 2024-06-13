from collections import Counter

class Solution:
    # relative sort with different items sorted in ascending order appended at the end

    # fastest
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # counting sort
        freqs = Counter(arr1)
        _max = max(arr1)
        _min = min(arr1)

        i = 0
        # add the numbers in relative order
        for num in arr2:
            for _ in range(freqs[num]):
                arr1[i] = num
                freqs[num] -= 1
                i += 1
        
        # add the different ones
        for num in range(_min, _max + 1):
            while freqs[num] > 0:
                arr1[i] = num
                freqs[num] -= 1
                i += 1
        
        return arr1


    # cool solution
    def relativeSortArray2(self, arr1: list[int], arr2: list[int]) -> list[int]:
        present_elems_pos = {}
        arr1_len = len(arr1)

        for i in range(len(arr2)):
            present_elems_pos[arr2[i]] = i
        
        def relativeSort(x):
            if x in present_elems_pos:
                return present_elems_pos[x]
            return x + arr1_len

        arr1.sort(key=relativeSort)

        return arr1

    def relativeSortArray3(self, arr1: list[int], arr2: list[int]) -> list[int]:
        
        freqs = {}

        # arr2 has unique items, identify them
        for num in arr2:
            freqs[num] = 0

        different_nums = []
        # count the f of each unique item
        for num in arr1:
            if num not in freqs:
                different_nums.append(num)
            else:
                freqs[num] += 1
        
        i = 0
        for num, f in freqs.items():
            for _ in range(f):
                arr1[i] = num
                i += 1
        
        # attach the different ones
        different_nums.sort()
        for num in different_nums:
            arr1[i] = num
            i += 1
        
        return arr1

s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))