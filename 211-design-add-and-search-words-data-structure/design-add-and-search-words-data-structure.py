class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i+1)
            else:
                for c in node.children.values():
                    if dfs(c, i+1):
                        return True
                return False
        
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)