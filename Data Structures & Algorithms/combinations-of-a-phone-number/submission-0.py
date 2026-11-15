class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subset = []
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []
        
        def dfs(index):
            if index == len(digits):
                res.append(''.join(subset))
                return

            letters = digit_map[digits[index]]

            for letter in letters:
                subset.append(letter)
                dfs(index + 1)
                subset.pop()

        dfs(0)
        return res
