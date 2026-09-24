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
        def dfs(i, node):
            if i == len(word):
                return node.endOfWord
            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                return dfs(i+1, node)
            else:
                for c in node.children.values():
                    if dfs(i+1, c):
                        return True
                return False
        
        return dfs(0, self.root)

            





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)