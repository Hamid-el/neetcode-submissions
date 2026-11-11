class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return

            for j in range(i, len(nums)):  # right path/child
                if total + nums[j] > target: #works becasue of sorting
                    break

                subset.append(nums[j])
                dfs(j, total + nums[j])  # left path/child in tree, include nums[j], stay at j to allow reuse
                subset.pop()  # go back to parent again

        dfs(0, 0)
        return res

             