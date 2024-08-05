from collections import deque

# https://leetcode.com/problems/alien-dictionary/
class Solution:
    # the key was to represent the dependency between the nodes by finding the first
    # difference in adjacent string pairs
    def alienOrder(self, words: list[str]) -> str:
        # nodes are the letters
        # edges are the dependencies between letters
        # kahns topological sort

        nodes = set(''.join(words))
        adj_list = {ch: [] for ch in nodes}
        indegrees = {ch: 0 for ch in nodes}
        queue = deque()

        # add edges between chrs in words
        for i in range(len(words) - 1):
            word_a = words[i]
            word_b = words[i + 1]
            ptr = 0
            found_missmatch = False
            # find the first different char, this is an edge
            while ptr < len(word_a) and ptr < len(word_b):
                if word_a[ptr] != word_b[ptr]:
                    found_missmatch = True
                    break # ptr is pointing to first difference
                ptr += 1
            if found_missmatch:
                indegrees[word_b[ptr]] += 1
                adj_list[word_a[ptr]].append(word_b[ptr])
            elif len(word_a) > len(word_b):  # word_b is a prefix of word_a, ex: ['abc', 'ab']
                return ''

        for node in nodes:
            if indegrees[node] == 0:
                queue.append(node)
        
        lex_order = []
        while queue:
            node = queue.popleft()
            lex_order.append(node)
            
            for neighbor in adj_list[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        lex_order = ''.join(lex_order)
        return lex_order if len(lex_order) == len(nodes) else ''