class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            max_dp[i] = max(
                current,
                current * max_dp[i - 1],
                current * min_dp[i - 1]
            )

            min_dp[i] = min(
                current,
                current * max_dp[i - 1],
                current * min_dp[i - 1]
            )

            result = max(result, max_dp[i])

        return result