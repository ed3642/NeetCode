from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        
        @lru_cache(maxsize=None)
        def min_difficulty(job_i, days_left):
            nonlocal n

            if days_left == 1:
                return hardest_remaining[job_i]

            best = float('inf')
            hardest = jobDifficulty[job_i]
            max_index = n - days_left
            for i in range(job_i, max_index + 1):
                hardest = max(hardest, jobDifficulty[i])
                best = min(best, min_difficulty(i + 1, days_left - 1) + hardest)
            
            return best

        n = len(jobDifficulty)
        if d > n:
            return -1
        hardest_remaining = [0] * n
        hardest = -float('inf')
        for i in range(n - 1, -1, -1):
            hardest = max(hardest, jobDifficulty[i])
            hardest_remaining[i] = hardest
        
        return min_difficulty(0, d)