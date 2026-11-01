class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = [] # index
        
        for i in range(len(nums)):
            if dq and dq[0] <= i - k:
                dq.popleft() # out of intervall

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop() # nums[i] is smaller than curr max
            
            dq.append(i)
            if i >= k - 1:
                    res.append(nums[dq[0]])    

        return res
            
