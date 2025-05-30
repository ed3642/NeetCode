# https://leetcode.com/problems/word-ladder

from collections import defaultdict, deque
from typing import List

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # make neighbors based on wildcard and just bfs
        
        if endWord not in wordList:
            return 0

        N = len(wordList)
        adj_list = defaultdict(list)
        adj_list[beginWord] = []

        for word in wordList:
            for j in range(len(word)):
                wildcard = word[:j] + '*' + word[j + 1:]
                adj_list[wildcard].append(word)
        
        q = deque([beginWord])
        visited = set()
        steps = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                visited.add(word)

                for i in range(len(word)):
                    wildcard = word[:i] + '*' + word[i + 1:]
                    for nei in adj_list[wildcard]:
                        if nei not in visited:
                            if nei == endWord:
                                return steps + 1
                            q.append(nei)
                            visited.add(nei)
            
            steps += 1

        return 0

    # TLE
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def are_neighbors(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
                    if count > 1:
                        return False
            return count == 1
        
        if endWord not in wordList:
            return 0

        N = len(wordList)
        adj_list = {word: [] for word in wordList}
        adj_list[beginWord] = []

        for i in range(N):
            if are_neighbors(beginWord, wordList[i]):
                adj_list[beginWord].append(wordList[i])
            for j in range(N):
                if i != j:
                    if are_neighbors(wordList[i], wordList[j]):
                        adj_list[wordList[i]].append(wordList[j])
        
        q = deque([beginWord])
        visited = set()
        steps = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                visited.add(word)

                for nei in adj_list[word]:
                    if nei not in visited:
                        if nei == endWord:
                            return steps + 1
                        q.append(nei)
                        visited.add(nei)
            
            steps += 1

        return 0