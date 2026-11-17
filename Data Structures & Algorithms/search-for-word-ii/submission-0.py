class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
         
        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row, col, node):
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] == "#"):
                return

            ch = board[row][col]
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # found a complete word
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None

            temp = board[row][col]
            board[row][col] = "#"

            dfs(row - 1, col, next_node)
            dfs(row + 1, col, next_node)
            dfs(row, col - 1, next_node)
            dfs(row, col + 1, next_node)

            board[row][col] = temp

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result
