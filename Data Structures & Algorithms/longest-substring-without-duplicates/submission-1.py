class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcadef
        seen = {} # char -> index
        left = 0
        longest = 0

        for right, ch  in enumerate(s):
            if ch in seen:
                # which char was seen firstly after duplicate char or left
               left = max(seen[ch]+1, left)
                
            seen[ch] = right
            longest = max(longest, right - left + 1)
        
        return longest