import heapq

class Solution:
    def findMaximizedCapital(self, k: int, budget: int, profits: list[int], capital: list[int]) -> int:
        # put the ones that we can afford in a heap and finish the best project
        # repeat with new bigger budget until k projects are done

        def insert_affordable(budget):
            nonlocal index
            while index < len(profits) and projects[index][0] <= budget:
                heapq.heappush(heap, -projects[index][1])
                index += 1


        projects = list(zip(capital, profits))
        projects.sort()
        heap = [] # ordered by profit

        # insert the projects that we can afford innitially
        index = 0
        insert_affordable(budget)
        
        while heap and k > 0:
            profit = -heapq.heappop(heap)
            budget += profit
            insert_affordable(budget)
            k -= 1
        
        return budget

s = Solution()
print(s.findMaximizedCapital(1,0,[1,2,3],[1,1,2]))