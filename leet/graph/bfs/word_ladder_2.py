# https://leetcode.com/problems/word-ladder-ii

from collections import defaultdict, deque
from typing import List

class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def bt(word, builder):
            if word == beginWord:
                res.append(builder.copy())
                return
            
            for parent in parents[word]:
                builder.append(parent)
                bt(parent, builder)
                builder.pop()

        def find_min_dist():
            q = deque([beginWord])
            visited = set([beginWord])
            found_path = False

            while q:
                next_level = set()
                for _ in range(len(q)):
                    word = q.popleft()

                    for i in range(len(word)):
                        wildcard = word[:i] + '*' + word[i + 1:]
                        for nei in adj_list[wildcard]:
                            if nei not in visited:
                                next_level.add(nei)
                                parents[nei].append(word)
                                if nei == endWord:
                                    found_path = True
                if found_path:
                    return True
                visited.update(next_level)
                q.extend(next_level)
            return False

        if endWord not in wordList:
            return []
        res = []
        adj_list = defaultdict(list)
        parents = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + '*' + word[i + 1:]
                adj_list[wildcard].append(word)

        if not find_min_dist():
            return []
        
        bt(endWord, [endWord])
        for path in res:
            path.reverse()
        return res

    # MLE
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []
        res = []
        adj_list = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + '*' + word[i + 1:]
                adj_list[wildcard].append(word)

        q = deque([(beginWord, [beginWord])]) # word, path
        depth = 0
        visited = set()

        while q:
            for _ in range(len(q)):
                word, path = q.popleft()
                visited.add(word)

                for i in range(len(word)):
                    wildcard = word[:i] + '*' + word[i + 1:]
                    for nei in adj_list[wildcard]:
                        if nei not in visited:
                            q.append((nei, path + [nei]))
                            if nei == endWord:
                                res.append(path + [nei])
            # this level found the shortest paths
            if res:
                return res
            depth += 1
        
        return res
