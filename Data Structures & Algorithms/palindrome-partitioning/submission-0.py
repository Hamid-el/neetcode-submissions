class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []

        # precompute whether every substring is a palindrome
        is_palindrome = [[False] * len(s) for _ in range(len(s))]

        for start in range(len(s) - 1, -1, -1):
            for end in range(start, len(s)):
                if s[start] == s[end] and (
                    end - start <= 2 or is_palindrome[start + 1][end - 1]
                ):                      # eg "abba" uses result from "bb"
                    is_palindrome[start][end] = True

        def dfs(start_index):
            if start_index == len(s):
                result.append(subset .copy())
                return

            for end_index in range(start_index, len(s)):
                if not is_palindrome[start_index][end_index]:
                    continue

                subset.append(s[start_index:end_index + 1])
                dfs(end_index + 1)
                subset .pop()

        dfs(0)
        return result