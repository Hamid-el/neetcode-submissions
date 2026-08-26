class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        # {1:3, 2:2, 3:1}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
             
        # [[],[3],[2],[1],[]...]
        #      1   2   3 times 
        # go from left to right because rightest elem has highest appereance
        for num, amount in hash.items():
            freq[amount].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        