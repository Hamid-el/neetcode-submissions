class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0

        while left < right:
            # finde nächsten rechten block der höher ist
            if height[left] < height[right]:
                left_max = max(left_max, height[left]) # hightest hight on left from pointer pov
                area += max(0, left_max - height[left]) # max eig unnötig, da zeile 11 ja schon left_max größer als height[left] ist also die subtraktion immer min 0 ist falls beide gleich groß sind
                left += 1
            else:
                right_max = max(right_max, height[right])
                area += max(0, right_max - height[right]) 
                right -= 1 
            
        return area