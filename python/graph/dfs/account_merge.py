# https://leetcode.com/problems/accounts-merge

from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def dfs(node, visited: set):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj_list[node]:
                dfs(nei, visited)
            
            return visited
        
        adj_list = defaultdict(list)
        names = {}
        root_emails = set()

        for acc in accounts:
            name = acc[0]
            root_email = acc[1]
            names[root_email] = name
            root_emails.add(root_email)
            for email in acc[2:]:
                adj_list[root_email].append(email)
                adj_list[email].append(root_email)

        res = []
        visited_emails = set()
        for email in root_emails:
            if email not in visited_emails:
                group = dfs(email, set())
                visited_emails.update(group)
                res.append([names[email]] + sorted(group))

        return res