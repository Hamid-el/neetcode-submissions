class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 = [1, 3, 8], nums2 = [2, 4, 9, 10]
        #
        # nums1 = [1, 3 | 8] -> | not before 3 because r = len(nums1)
        # nums2 = [2, 4 | 9, 10]
        #
        # Left side:  [1, 2, 3, 4]
        # Right side: [8, 9, 10]
        # Median = 4 (odd total number of elements)
        # hälft von total length - linke hälft von kleinerem array = wieviele elem man links braucht von größerem array

        # bin search on smaller array, should be nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1)

        while l <= r:
            mid1 = (l + r) // 2
            mid2 = (len(nums1) + len(nums2) + 1) // 2 - mid1

            left1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            right1 = float('inf') if mid1 == len(nums1) else nums1[mid1]
            left2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            right2 = float('inf') if mid2 == len(nums2) else nums2[mid2]

            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                r = mid1 - 1
            else:
                l = mid1 + 1