class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        
        # build Trie
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
        
        m, n = len(board), len(board[0])
        ans = set()
        visited = set()
        
        def dfs(i, j, node, word):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or board[i][j] not in node.children:
                return
            visited.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]

            if node.endOfWord:
                ans.add(word)
            
            dfs(i+1, j, node, word)
            dfs(i-1, j, node, word)
            dfs(i, j+1, node, word)
            dfs(i, j-1, node, word)

            visited.remove((i, j))
            

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
            
        return list(ans)