from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.products = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.products.append(word)
            node.products.sort()
            if len(node.products) > 3:
                node.products.pop()
    
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.products

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        prefix = ''
        result = []
        for char in searchWord:
            prefix += char
            suggestions = trie.search(prefix)
            result.append(suggestions)
        return result

### above gets suggestions all at once and doesnt have to traverse the tree multiple times
### Get suggestions each character input, slower ###

class TrieNode2:
    def __init__(self, val='', is_leaf=False):
        self.val = val
        self.children = [None] * 26 # non-null represents this child char is present
        self.is_leaf = is_leaf

class Trie2:

    def __init__(self):
        self.root = TrieNode()

        self.ch_mappings = defaultdict(int)
        alphabet = 'abcdefghijklmnopqrstuvwxyz' # lexilogically sorted alphabet
        for i, ch in enumerate(alphabet):
            self.ch_mappings[ch] = i

    def insert(self, word):
        if len(word) < 1:
            return
        
        node = self.root
        for ch in word:
            ch_mapping = self.ch_mappings[ch]
            
            if node.children[ch_mapping] == None:
                node.children[ch_mapping] = TrieNode(ch)
            node = node.children[ch_mapping]

        node.is_leaf = True # last char in word

    def suggest(self, prefix: str):
        
        def dfs(node: TrieNode, builder: list):
            # just finish the word with lexilogically smallest
            #print(builder)
            if len(suggestions) == 3:
                return
            
            if node.is_leaf:
                suggestions.append(''.join(builder))
                if len(suggestions) == 3:
                    return
            
            for child in node.children:
                if child:
                    builder.append(child.val)
                    dfs(child, builder)
                    builder.pop()

        if len(prefix) == 0:
            return []
        
        # match all chars in the prefix, must match the entire prefix
        root = self.root
        for ch in prefix: 
            ch_mapping = self.ch_mappings[ch]

            if not root.children[ch_mapping]:
                return []
            root = root.children[ch_mapping]
        
        
        suggestions = []
        dfs(root, list(prefix))
        return suggestions

class Solution2:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        product_trie = Trie()

        for product in products:
            product_trie.insert(product)

        res = []
        for i in range(len(searchWord)):
            res.append(product_trie.suggest(searchWord[:i + 1]))
        
        return res