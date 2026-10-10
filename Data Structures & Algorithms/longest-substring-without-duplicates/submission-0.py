class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # char -> index
        left = 0
        res = 0
        for right, ch in enumerate(s):
            if ch in seen:
                left = max(seen[ch] + 1, left)
            seen[ch] = right
            res = max(res, right - left + 1)
        
        return res