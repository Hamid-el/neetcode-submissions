class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(houses):
            if len(houses) == 1:
                return houses[0]

            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                            #dont rob     rob
                dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])

            return dp[len(houses) - 1]

        if len(nums) == 1: #nochmal nötig, sonst indexerror bei leeren array
            return nums[0]

        case_one = rob_linear(nums[:-1])
        case_two = rob_linear(nums[1:])

        return max(case_one, case_two)