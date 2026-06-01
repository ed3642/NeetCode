from collections import defaultdict, deque
import math
from typing import List

# SPF lets us generate the prime factors of a num x in log x time
# spf is made in O(n log (log n)) time, kinda complicated derivation for that time
# for minJumps solution
MAX_NUM = 1000001
spf = [i for i in range(MAX_NUM)]

for i in range(2, int(math.sqrt(MAX_NUM)) + 1):
    if spf[i] == i:
        for j in range(i * i, MAX_NUM, i):
            if spf[j] == j:
                spf[j] = i

# prime factor sieve, factor nums into their primes in O(n log n)
# for minJumps2 solution
MAX_NUM = 1000001
factors = [[] for _ in range(MAX_NUM)]
for i in range(2, MAX_NUM):
    if not factors[i]:
        for j in range(i, MAX_NUM, i):
            factors[j].append(i)
            
class Solution:

    def minJumps(self, nums: List[int]) -> int:
        
        g = defaultdict(list)

        for i, num in enumerate(nums):
            while num > 1:
                # generates prime factors of num in O(log num) time
                g[spf[num]].append(i)
                num = num // spf[num]
        
        n = len(nums)
        q = deque([0])
        steps = 0
        visited = [False] * n
        visited[0] = True

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == n - 1:
                    return steps

                if node > 0 and not visited[node - 1]:
                    q.append(node - 1)
                    visited[node - 1] = True
                if node < n - 1 and not visited[node + 1]:
                    q.append(node + 1)
                    visited[node + 1] = True
                # prime neighbors
                if spf[nums[node]] == nums[node]: # is prime
                    for i in g[nums[node]]:
                        if not visited[i]:
                            q.append(i)
                            visited[i] = True
                    g[nums[node]].clear() # only need to use once, save time by not iter again
            steps += 1
        
        return -1 # shouldnt happen

    def minJumps2(self, nums: List[int]) -> int:

        g = defaultdict(list)
        visited = [False] * len(nums)

        for i, num in enumerate(nums):
            for p in factors[num]:
                g[p].append(i)
        
        q = deque([0])
        visited[0] = True
        steps = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == len(nums) - 1:
                    return steps

                if node - 1 >= 0:
                    if not visited[node - 1]:
                        q.append(node - 1)
                        visited[node - 1] = True
                if node + 1 < len(nums):
                    if not visited[node + 1]:
                        q.append(node + 1)
                        visited[node + 1] = True
                if len(factors[nums[node]]) == 1:
                    p = nums[node]
                    for nei in g[p]:
                        if not visited[nei]:
                            q.append(nei)
                            visited[nei] = True
                    del g[p] # optimization, only use once
            steps += 1
        
        return -1 # shouldnt happen

    # TLE
    def minJumps(self, nums: List[int]) -> int:

        # sieve, primes [2, n]
        def gen_primes(n):
            primes = set()
            non_primes = set()

            p = 2
            while p * p <= n:
                if p not in non_primes:
                    primes.add(p)
                    for val in range(p * p, n + 1, p):
                        non_primes.add(val)
                p += 1
            for val in range(p, n + 1):
                if val not in non_primes:
                    primes.add(val)
            return primes
        
        primes = gen_primes(max(nums))

        g = {p: [] for p in primes}
        visited = [False] * len(nums)

        for i, num in enumerate(nums):
            for p in primes:
                if num % p == 0:
                    g[p].append(i)
        
        q = deque([0])
        visited[0] = True
        steps = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == len(nums) - 1:
                    return steps

                if node - 1 >= 0:
                    if not visited[node - 1]:
                        q.append(node - 1)
                        visited[node - 1] = True
                if node + 1 < len(nums):
                    if not visited[node + 1]:
                        q.append(node + 1)
                        visited[node + 1] = True
                if nums[node] in g:
                    for nei in g[nums[node]]:
                        if not visited[nei]:
                            q.append(nei)
                            visited[nei] = True
                    del g[nums[node]] # optimization, only use once
            steps += 1
        
        return -1 # shouldnt happen

    # TLE
    def minJumps2(self, nums: List[int]) -> int:
        
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2 or n == 3 or n == 5:
                return True
            if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
                return False
            
            # +2 to make sure range is right
            # this is the 6k +-1 prime check
            for i in range(6, int(math.sqrt(n)) + 2, 6):
                if n % (i + 1) == 0 or n % (i - 1) == 0:
                    return False
            return True

        primes = []
        for num in nums:
            if is_prime(num):
                primes.append(num)

        g = {p: [] for p in primes}
        visited = [False] * len(nums)

        for i, num in enumerate(nums):
            for p in primes:
                if num % p == 0:
                    g[p].append(i)
        
        q = deque([0])
        visited[0] = True
        steps = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == len(nums) - 1:
                    return steps

                if node - 1 >= 0:
                    if not visited[node - 1]:
                        q.append(node - 1)
                        visited[node - 1] = True
                if node + 1 < len(nums):
                    if not visited[node + 1]:
                        q.append(node + 1)
                        visited[node + 1] = True
                if nums[node] in g:
                    for nei in g[nums[node]]:
                        if not visited[nei]:
                            q.append(nei)
                            visited[nei] = True
                    g[nums[node]] = [] # clear so only check once
            steps += 1
        
        return -1 # shouldnt happen
