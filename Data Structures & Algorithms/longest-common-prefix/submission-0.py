class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = PrefixTree()
        res = ''

        for s in strs:
            trie.insert(s)
        
        curr = trie.root
        while len(curr.children) == 1 and not curr.isWord:
            char = list(curr.children.keys())[0]
            res += char
            curr = curr.children[char]

        return res