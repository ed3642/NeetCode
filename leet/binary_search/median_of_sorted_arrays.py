from typing import List

class Solution:
    # WIP
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def find_kth_smallest(l, r, l2, r2, k):
            size1 = r - l + 1
            size2 = r2 - l2 + 1

            if size1 == 0:
                return nums2[l2 + k]
            if size2 == 0:
                return nums1[l + k]
            if k == 0:
                return min(nums1[l], nums2[l2])

            next_l = min(r - 1, k // 2)
            next_l2 = min(r2 - 1, k // 2)

            if nums1[next_l] < nums2[next_l2]:
                return find_kth_smallest(next_l + 1, r, l2, r2, k - (next_l + 1))
            return find_kth_smallest(l, r, next_l2 + 1, r2, k - (next_l2 + 1))
        
        n = len(nums1)
        m = len(nums2)
        total_size = n + m
        total_is_odd = total_size % 2 != 0
        need_to_cut = (total_size // 2)

        if total_is_odd:
            return find_kth_smallest(0, n - 1, 0, m - 1, need_to_cut)
        else:
            return (find_kth_smallest(0, n - 1, 0, m - 1, need_to_cut - 1) + find_kth_smallest(0, n - 1, 0, m - 1, need_to_cut)) / 2
    
def findKth(nums1, nums2, k):
    if not nums1:
        return nums2[k]
    if not nums2:
        return nums1[k]
    if k == 0:
        return min(nums1[0], nums2[0])
    i = min(len(nums1) - 1, k // 2)
    j = min(len(nums2) - 1, k // 2)
    if nums1[i] < nums2[j]:
        return findKth(nums1[i+1:], nums2, k - (i + 1))
    else:
        return findKth(nums1, nums2[j+1:], k - (j + 1))

def findMedianSortedArrays(nums1, nums2):
    n = len(nums1) + len(nums2)
    if n % 2 == 1:
        return findKth(nums1, nums2, n // 2)
    else:
        return (findKth(nums1, nums2, n // 2 - 1) + findKth(nums1, nums2, n // 2)) / 2