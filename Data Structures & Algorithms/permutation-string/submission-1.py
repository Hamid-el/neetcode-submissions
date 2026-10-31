class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True

        for right in range(len(s1), len(s2)):
            s2_counter[s2[right]] += 1 # add new char right
            s2_counter[s2[right - len(s1)]] -= 1 # remove char left

            if s1_counter == s2_counter:
                return True

        return False