class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1) 
        for left in range(len(s2) - len(s1) + 1):
            right = left + len(s1)
            s2_counter = Counter(s2[left:right])
            if s1_counter == s2_counter:
                return True
        
        return False