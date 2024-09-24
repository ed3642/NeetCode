from typing import List

class Node:
    def __init__(self, val=''):
        self.val = val
        self.children = {}

class Trie:
    def __init__(self):
        self.dummy_root = Node()

    def insert(self, string: str):
        node = self.dummy_root
        for ch in string:
            if ch not in node.children:
                node.children[ch] = Node(ch)
            node = node.children[ch]

    def search(self, string: str):
        node = self.dummy_root
        max_depth = 0
        for i, ch in enumerate(string):
            if ch in node.children:
                node = node.children[ch]
                max_depth = i + 1
            else:
                return max_depth
        return max_depth
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        # trie from arr1 and see max depth from elems in arr2
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))
        
        max_depth = 0
        for num in arr2:
            max_depth = max(trie.search(str(num)), max_depth)

        return max_depth
