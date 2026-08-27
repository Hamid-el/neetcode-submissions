class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        answer = [1] * n
        l = [1] * n
        r = [1] * n        
        
        for i in range(1, n):
            l[i] = l[i - 1] *  nums[i - 1]  
        
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]
        
        for i in range(n):
            answer[i] = l[i] * r[i]

        return answer
        