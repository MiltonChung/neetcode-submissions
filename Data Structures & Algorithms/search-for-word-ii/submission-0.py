class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
    
    # def searchPrefix(self, prefix): # [isInPrefix, isWord]
    #     curr = self.root

    #     for c in prefix:
    #         if c not in curr.children:
    #             return [False, False]
    #         curr = curr.children[c]
    #     return [True, curr.isWord]
    
    # def isLastNode(self, node):
    #     return len(node.children.values()) == 0

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = []
        visit = set()

        trie = Trie()
        for word in words: 
            trie.addWord(word)

        def dfs(r, c, node, path):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (r, c) in visit:
                return

            char = board[r][c]
            childNode = node.children.get(char)
            if not childNode: return

            visit.add((r, c))

            if childNode.isWord:
                res.append(path + char)
                childNode.isWord = False

            dfs(r + 1, c, childNode, path + char)
            dfs(r - 1, c, childNode, path + char)
            dfs(r, c + 1, childNode, path + char)
            dfs(r, c - 1, childNode, path + char)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root, "")

        return res














