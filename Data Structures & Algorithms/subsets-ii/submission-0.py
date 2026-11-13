class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(start_index):
            #if start_index >= len(nums):
            res.append(subset.copy())
             #   return

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
            
        dfs(0)
        return res