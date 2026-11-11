class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1) # left path/child in tree, include nums[i]
            subset.pop() # go back to parten again
            dfs(i + 1) # right path/child in tree, do not include nums[i], include []

        dfs(0)
        return res