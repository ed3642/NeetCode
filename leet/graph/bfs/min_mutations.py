# https://leetcode.com/problems/minimum-genetic-mutation
from collections import defaultdict, deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        # define a neighbor as the genes that are one off from node
        # find shortest path from startGene to endGene
        # BFS will do since all edges are weight 1

        def is_one_off(gene, other):
            off = 0
            for i in range(len(gene)):
                if gene[i] != other[i]:
                    off += 1
                if off > 1:
                    return False
            return off == 1

        if startGene == endGene:
            return 0
        elif len(bank) == 0:
            return -1

        adj_list = defaultdict(list)
        if startGene not in bank:
            bank.append(startGene)

        # get neighbors
        N = len(bank)
        for i, gene in enumerate(bank):
            for j in range(N):
                other = bank[j]
                if i != j and is_one_off(gene, other):
                    adj_list[gene].append(other)

        # bfs
        q = deque([startGene])
        visited = set([startGene])
        depth = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj_list[node]:
                    # found end_gene
                    if nei == endGene:
                        return depth
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            depth += 1
        
        return -1