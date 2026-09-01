#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    TrieNode* neighbor[26] = {nullptr};
    bool isLeaf = false;
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->neighbor[c-'a'] == nullptr)
                node->neighbor[c-'a'] = new TrieNode();
            node = node->neighbor[c-'a'];
        }
        node->isLeaf = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->neighbor[c-'a'] == nullptr)
                return false;
            node = node->neighbor[c-'a'];
        }
        return node->isLeaf ? true : false;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->neighbor[c-'a'] == nullptr)
                return false;
            node = node->neighbor[c-'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */