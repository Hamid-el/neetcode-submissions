class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
    
       # s_counter = Counter(s[:len(t)])
        s_counter = Counter()
        t_counter = Counter(t)

        left = 0
        min_size = float("inf")
        res = ""
        required = len(t_counter)
        formed = 0

        for right in range(len(s)):
            s_counter[s[right]] += 1

            if s[right] in t_counter and s_counter[s[right]] == t_counter[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_size:
                    min_size = right - left + 1
                    res = s[left:right + 1]

                if s[left] in t_counter and s_counter[s[left]] == t_counter[s[left]]:
                    formed -= 1

                s_counter[s[left]] -= 1
                left += 1

        return res
