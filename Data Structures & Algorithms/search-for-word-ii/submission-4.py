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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (r, c) in visit:
                return

            char = board[r][c]
            if char not in node.children:
                return

            word += char
            newNode = node.children[char]
            if newNode.isWord:
                res.add(word)
                newNode.isWord = False
            
            visit.add((r, c))

            dfs(r + 1, c, newNode, word)
            dfs(r - 1, c, newNode, word)
            dfs(r, c + 1, newNode, word)
            dfs(r, c - 1, newNode, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root, '')

        return list(res)











