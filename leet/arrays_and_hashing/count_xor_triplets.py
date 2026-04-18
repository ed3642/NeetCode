class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        # if a subseq xors to 0, there are length - 1 triplets in there
        # a ^ b ^ c = 0
        # b ^ c = a (triplet 1)
        # c = a ^ b (triplet 2)
        
        k = 1
        n = len(arr)
        total_count = 0

        for i in range(n - 1):
            subseq = arr[i]
            for k in range(i + 1, n):
                subseq ^= arr[k]
                if subseq == 0:
                    length = k - i + 1
                    total_count += length - 1

        return total_count

    def countTriplets(self, arr: list[int]) -> int:
        # keep track of a and b totals
        # try all i and k pairs and just move j inbetween them
        # brute force O(n^3)

        def check_j_positions(i, k, a, b):
            if k - i < 1:
                return 0
            j = i + 1
            count = 0
            while j <= k:
                a ^= arr[j] # adds jth to a
                b ^= arr[j] # cancels out the jth from b
                if a == b:
                    count += 1
                j += 1
            return count

        k = 1
        n = len(arr)
        total_count = 0

        for i in range(n - 1):
            a = arr[i]
            b = 0
            for k in range(i + 1, n):
                b ^= arr[k]
                total_count += check_j_positions(i, k, a, b)
        
        return total_count