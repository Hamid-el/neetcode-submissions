class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for p in points:
            dist = math.sqrt((p[0]-0)**2 + (p[1]-0)**2)
            heapq.heappush(heap, (-dist, p))

            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        for dist, p in heap:
            res.append(p)
 
        return res