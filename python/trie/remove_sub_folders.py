# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
from typing import List

class Node:
    def __init__(self, val='', is_leaf=False):
        self.val = val
        self.is_leaf = is_leaf
        self.children = {}

class Trie:
    def __init__(self):
        self.dummy_head = Node()
    
    def insert(self, path):
        node = self.dummy_head
        for name in path:
            if name not in node.children:
                node.children[name] = Node(name)
                node = node.children[name]
            elif name in node.children:
                if node.children[name].is_leaf:
                    return False
                node = node.children[name]
        node.is_leaf = True
        return True

class Solution:
    # O(nlogn + n * L) -> O(n * L) where L = avg(path_length)
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        # format paths
        folder.sort(key=lambda x: len(x))
        paths = [None] * len(folder)
        for f_i, path in enumerate(folder):
            i = 0
            paths[f_i] = path.split('/')
        
        trie = Trie()
        res = []
        for i, path in enumerate(paths):
            if trie.insert(path):
                res.append(folder[i])

        return res
    