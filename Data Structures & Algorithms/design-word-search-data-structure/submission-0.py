class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(index, node):
            if index == len(word):
                return node.is_end

            ch = word[index]
            if ch == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)

