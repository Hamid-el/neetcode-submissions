class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = {} # num -> index
        left = 0
        right = len(nums) - 1
        for index, num in enumerate(nums):
            #target = -nums[left] - nums[mid]
            if num > 0:
                break
              # needed, else nums[-1]
            if index > 0 and nums[index] == nums[index-1]:
                continue

            left = index + 1
            right = len(nums) - 1
            # 2sum 2
            while left < right:
                total = nums[index] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # or use res = set() for no dublicates + return as list
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return res

