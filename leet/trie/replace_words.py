from collections import defaultdict

class TrieNode:
    def __init__(self, val='', is_leaf=False):
        self.val = val
        self.is_leaf = is_leaf
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.is_leaf = True
    
    # like normal prefix_search but keep track of last_checked node
    # 0 for false, 1 for true, 2 for true and is word
    # also return the last checked node
    def prefix_search(self, prefix_ch, start_node=None):
        node = self.root if start_node == None else start_node
        if prefix_ch not in node.children:
            return (0, None)
        node = node.children[prefix_ch]
        return (2, None) if node.is_leaf else (1, node)

class Solution:
    # Trie
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        words = sentence.split(' ')
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        for i in range(len(words)):
            word = words[i]
            last_checked_node = None # to not have to start from root each time
            for j in range(len(word)):
                prefix_ch = word[j]
                result, last_checked_node = trie.prefix_search(prefix_ch, last_checked_node)
                if result == 0: # dead end
                    break
                elif result == 1: # can keep searching
                    continue
                elif result == 2: # found it
                    words[i] = word[:j + 1]
                    break
        
        return ' '.join(words)

    # brute force, good enough for the test cases
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        
        word_set = set(dictionary)
        words = sentence.split(' ')

        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                prefix_word = word[:j + 1]
                if prefix_word in word_set:
                    words[i] = prefix_word
                    break

        return ' '.join(words)