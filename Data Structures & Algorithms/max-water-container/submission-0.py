class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1 

        while left < right:
            h = min(heights[right], heights[left])
            new_area = h * (right - left)
            area = max(area, new_area)

            if heights[left] < heights[right]:
                 left += 1
            else:
                right -= 1
                
        return area