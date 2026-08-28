class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        max_counter = 0
        # i=0
        # nums[i]=100-> abbruch
        # ...
        # i=3
        # nums[i]= 1 -> i = 4, counter = 1, nums[i]=
        for i in range(len(nums)):
            
            counter = 1
            curr = nums[i]

            if (curr - 1) not in n:
                while curr + 1 in n:
                    #print(curr +1)
                    curr += 1
                    counter += 1
                max_counter = max(max_counter, counter)
        
        return max_counter