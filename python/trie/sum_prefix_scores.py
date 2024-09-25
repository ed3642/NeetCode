from typing import List

class Node:
    def __init__(self, val='', freq=1):
        self.val = val
        self.children = {}
        self.freq = freq

class Trie:
    def __init__(self):
        self.dummy_root = Node(freq=0)
    
    def insert(self, string):
        node = self.dummy_root
        for ch in string:
            if ch not in node.children:
                node.children[ch] = Node(ch)
            else:
                node.children[ch].freq += 1
            node = node.children[ch]

    def search(self, string):
        node = self.dummy_root
        total = 0
        for ch in string:
            if ch not in node.children:
                return total
            else:
                node = node.children[ch]
                total += node.freq
        return total

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        # trie with freq of prefix
        # then just sum path

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        for word in words:
            res.append(trie.search(word))

        return res