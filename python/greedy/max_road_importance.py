# https://leetcode.com/problems/maximum-total-importance-of-roads
class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        
        # sort by indegree and assign values from n to 1
        indegrees = [[0, i] for i in range(n)] # (indegress, node), so we can easily calc total later
        node_val = [0] * n

        for v1, v2 in roads:
            indegrees[v1][0] += 1
            indegrees[v2][0] += 1

        indegrees.sort(reverse=True)
        
        # assign node vals
        assign_val = n
        for _, node in indegrees:
            node_val[node] = assign_val
            assign_val -= 1

        total = 0
        for v1, v2 in roads:
            total += node_val[v1] + node_val[v2]
        
        return total