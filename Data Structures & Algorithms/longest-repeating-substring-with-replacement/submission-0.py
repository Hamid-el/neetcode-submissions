class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_freq = 0
        res = 0

        for right in range(len(s)):
            # no Counter. we only look t curr subset, not whole s
            count[s[right]] = count.get(s[right], 0) + 1 

            max_freq = max(max_freq, count[s[right]])
            # descrease subset until valid subset found (to use k on)
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
