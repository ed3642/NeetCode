class Node:
    def __init__(self, is_leaf=False):
        self.children = {}
        self.is_leaf = is_leaf

class WordDictionary:

    def __init__(self):
        self.dummy_head = Node()

    def addWord(self, word: str) -> None:
        node = self.dummy_head
        for ch in word:
            if not ch in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_leaf = True

    def search(self, word: str) -> bool:
        return self.search_from_node(word, self.dummy_head)

    def search_from_node(self, word: str, node: Node) -> bool:
        for i, ch in enumerate(word):
            if ch == '.':
                if i + 1 < len(word):
                    return any(self.search_from_node(word[i + 1:], child) for child in node.children.values())
                else: # last char is .
                    return any(child.is_leaf for child in node.children.values())
            else:
                if not ch in node.children:
                    return False
                node = node.children[ch]
        return node.is_leaf


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)