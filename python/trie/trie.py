# https://leetcode.com/problems/implement-trie-prefix-tree
class Node:
    def __init__(self, val='', is_leaf=False):
        self.val = val
        self.children = {}
        self.is_leaf = is_leaf

class Trie:
    # more efficient but less clear
    IS_LEAF_FLAG = 'ISLEAF'

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        children = self.root
        for c in word:
            if c not in children:
                children[c] = {Trie.IS_LEAF_FLAG: False}
            children = children[c]
        children[Trie.IS_LEAF_FLAG] = True

    def search(self, word: str) -> bool:
        children = self.root
        for c in word:
            if c not in children:
                return False
            children = children[c]
        return children[Trie.IS_LEAF_FLAG]

    def startsWith(self, prefix: str) -> bool:
        children = self.root
        for c in prefix:
            if c not in children:
                return False
            children = children[c]
        return True

class Trie2:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(val=c)
            node = node.children[c]
        node.is_leaf = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_leaf # the ending node must be a leaf

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)