class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        answer = [1] * n
        
        l = 1
        for i in range(n):
            answer[i] = l
            l *= nums[i] 

        r = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= r # like l * r
            r *= nums[i]

        return answer