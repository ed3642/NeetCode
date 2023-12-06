
class Node:
    def __init__(self, children=None, is_word=False):
        self.children = {} if not children else children
        self.is_word = is_word

class Trie:

    def __init__(self):
        self.dummy_head = Node()

    def insert(self, word: str) -> None:
        node = self.dummy_head
        for char in word:
            if not char in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_word = True # last char marks it as a word

    def search(self, word: str) -> bool:
        node = self.dummy_head
        for char in word:
            if not char in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.dummy_head
        for char in prefix:
            if not char in node.children:
                return False
            node = node.children[char]
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)