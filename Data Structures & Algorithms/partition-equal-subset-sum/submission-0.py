class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1) #dp[i] = True, wenn wir mit den bisher betrachteten Zahlen die Summe i bilden können, dh alle einträge in dp müssen schon True sein
        dp[0] = True

        for num in nums:
            for current_sum in range(target, num - 1, -1):
                #             are we alredy on target OR is num additionally needed to get target?
                dp[current_sum] = (dp[current_sum] or dp[current_sum - num])

        return dp[target]
