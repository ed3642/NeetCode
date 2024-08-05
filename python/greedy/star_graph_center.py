# https://leetcode.com/problems/find-center-of-star-graph/description/

from collections import defaultdict

class Solution:

    def findCenter(self, edges: list[list[int]]) -> int:
        
        # in the edge connections, there should be exactly one node that occurs n-1 times or one that occurs more than once
        # since its a 1 out star graph

        freqs = defaultdict(int)
        for v1, v2 in edges:
            freqs[v1] += 1
            freqs[v2] += 1
            if freqs[v1] > 1:
                return v1
            if freqs[v2] > 1:
                return v2

        return None

    # optimal solution
    # there is always one node that occurs twice in any pair of verticies.
    def findCenter(self, edges: list[list[int]]) -> int:
        first_edge, second_edge = edges[0], edges[1]

        return first_edge[0] if first_edge[0] in second_edge else first_edge[1]
        