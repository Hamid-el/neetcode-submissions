class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_counter = 0
        
        for num in num_set:
            # hat vorgänger = beginning of sequence, else is in middle of sequence
            if (num - 1) not in num_set:
                counter = 1
                while (num + counter) in num_set:
                    counter += 1
                max_counter = max(max_counter, counter)
       
        return max_counter