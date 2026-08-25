class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {} # element -> index
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hash:
                return [hash[rest], i]
            
            hash[nums[i]] = i