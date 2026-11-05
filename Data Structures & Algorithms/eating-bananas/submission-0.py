class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2 # bzw mid
            hours = sum(math.ceil(pile / k) for pile in piles) # // wegen aufrunden wichtig -> "will not eat any more bananas during this hour."

            if hours <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        
        return res