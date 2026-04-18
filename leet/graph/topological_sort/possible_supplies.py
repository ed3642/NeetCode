# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

from collections import defaultdict
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # topo sort

        adj_list = defaultdict(list)
        in_degree = defaultdict(int)

        for i, parts in enumerate(ingredients):
            for p in parts:
                adj_list[p].append(recipes[i])
                in_degree[recipes[i]] += 1

        # add in the supplies
        for p in supplies:
            if p not in in_degree:
                in_degree[p] = 0
        
        stack = []
        for node, deg in in_degree.items():
            if deg == 0:
                stack.append(node)

        all_possible = []
        while stack:
            node = stack.pop()
            all_possible.append(node)

            for nei in adj_list[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    stack.append(nei)
        
        # filter out the supplies from can_make
        can_make = []
        supply_set = set(supplies)
        for p in all_possible:
            if p not in supply_set:
                can_make.append(p)

        return can_make